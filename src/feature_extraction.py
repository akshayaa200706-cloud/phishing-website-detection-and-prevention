import re
import math
import socket
from urllib.parse import urlparse

import dns.resolver
import tldextract
import whois


# Features used by the trained models
FEATURES = [
    "entropy",
    "url_length",
    "num_www",
    "ratio_digits_url",
    "num_subdomains",
    "length_hostname",
    "random_domain",
    "num_dots",
    "num_hyphens",
    "ratio_digits_host",
    "prefix_suffix",
    "num_question_mark",
    "num_eq",
    "domain_age",
    "dns_resolvable",
    "num_ips",
    "ttl",
    "num_name_servers"
]


def calculate_entropy(text):
    """Calculate Shannon entropy of a string."""
    if not text:
        return 0.0

    probabilities = [
        text.count(char) / len(text)
        for char in set(text)
    ]

    return -sum(
        p * math.log2(p)
        for p in probabilities
        if p > 0
    )


def get_domain(url):
    """Extract hostname from URL."""
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)
    return parsed.hostname or ""


def get_domain_age(domain):
    """Calculate domain age in days using WHOIS."""
    try:
        information = whois.whois(domain)

        creation_date = information.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date is None:
            return -1

        from datetime import datetime

        if creation_date.tzinfo is not None:
            creation_date = creation_date.replace(tzinfo=None)

        age = datetime.now() - creation_date

        return max(age.days, -1)

    except Exception:
        return -1


def get_dns_information(domain):
    """
    Get DNS-related features:
    dns_resolvable
    num_ips
    ttl
    num_name_servers
    """

    dns_resolvable = 0
    num_ips = 0
    ttl = -1
    num_name_servers = 0

    # Get IP addresses
    try:
        answers = dns.resolver.resolve(domain, "A")

        dns_resolvable = 1
        num_ips = len(answers)

        if len(answers) > 0:
            ttl = answers.rrset.ttl

    except Exception:
        pass

    # Get name servers
    try:
        ns_answers = dns.resolver.resolve(domain, "NS")
        num_name_servers = len(ns_answers)
        dns_resolvable = 1

    except Exception:
        pass

    return (
        dns_resolvable,
        num_ips,
        ttl,
        num_name_servers
    )


def calculate_random_domain(hostname):
    """
    Estimate whether the hostname appears randomly generated.

    Returns:
        1 = likely random
        0 = likely normal
    """

    if not hostname:
        return 0

    # Remove common separators
    clean_hostname = re.sub(r"[^a-zA-Z0-9]", "", hostname)

    if len(clean_hostname) < 5:
        return 0

    entropy = calculate_entropy(clean_hostname)

    digit_count = sum(
        char.isdigit()
        for char in clean_hostname
    )

    digit_ratio = digit_count / len(clean_hostname)

    # Heuristic for unusually random-looking domains
    if entropy > 3.8 or digit_ratio > 0.30:
        return 1

    return 0


def extract_features(url):
    """
    Convert a URL into the 18 features required by the ML models.
    """

    if not isinstance(url, str):
        raise ValueError("URL must be a string.")

    url = url.strip()

    if not url:
        raise ValueError("URL cannot be empty.")

    # Add scheme if missing
    formatted_url = url

    if not formatted_url.startswith(("http://", "https://")):
        formatted_url = "http://" + formatted_url

    parsed = urlparse(formatted_url)

    hostname = parsed.hostname or ""

    if not hostname:
        raise ValueError("Could not extract a valid hostname from the URL.")

    # --------------------------------------------------
    # Basic URL features
    # --------------------------------------------------

    url_length = len(url)

    num_digits_url = sum(
        character.isdigit()
        for character in url
    )

    ratio_digits_url = (
        num_digits_url / url_length
        if url_length > 0
        else 0
    )

    num_www = hostname.lower().count("www")

    num_dots = url.count(".")

    num_hyphens = url.count("-")

    num_question_mark = url.count("?")

    num_eq = url.count("=")

    # --------------------------------------------------
    # Hostname features
    # --------------------------------------------------

    length_hostname = len(hostname)

    num_digits_host = sum(
        character.isdigit()
        for character in hostname
    )

    ratio_digits_host = (
        num_digits_host / length_hostname
        if length_hostname > 0
        else 0
    )

    # Extract registered domain and subdomain
    extracted = tldextract.extract(hostname)

    if extracted.subdomain:
        num_subdomains = len(
            extracted.subdomain.split(".")
        )
    else:
        num_subdomains = 0

    # Prefix/suffix feature
    prefix_suffix = 1 if "-" in hostname else 0

    # Random-looking domain
    random_domain = calculate_random_domain(hostname)

    # Entropy
    entropy = calculate_entropy(url)

    # --------------------------------------------------
    # DNS features
    # --------------------------------------------------

    (
        dns_resolvable,
        num_ips,
        ttl,
        num_name_servers
    ) = get_dns_information(hostname)

    # --------------------------------------------------
    # Domain age
    # --------------------------------------------------

    domain_age = get_domain_age(hostname)

    # --------------------------------------------------
    # Create feature dictionary
    # --------------------------------------------------

    features = {
        "entropy": entropy,
        "url_length": url_length,
        "num_www": num_www,
        "ratio_digits_url": ratio_digits_url,
        "num_subdomains": num_subdomains,
        "length_hostname": length_hostname,
        "random_domain": random_domain,
        "num_dots": num_dots,
        "num_hyphens": num_hyphens,
        "ratio_digits_host": ratio_digits_host,
        "prefix_suffix": prefix_suffix,
        "num_question_mark": num_question_mark,
        "num_eq": num_eq,
        "domain_age": domain_age,
        "dns_resolvable": dns_resolvable,
        "num_ips": num_ips,
        "ttl": ttl,
        "num_name_servers": num_name_servers
    }

    return features


# ------------------------------------------------------
# Test the feature extractor
# ------------------------------------------------------

if __name__ == "__main__":

    test_url = "https://google.com"

    print("=" * 60)
    print("PHISHING URL FEATURE EXTRACTION TEST")
    print("=" * 60)

    print("\nTesting URL:")
    print(test_url)

    try:
        extracted_features = extract_features(test_url)

        print("\nExtracted Features:")
        print("-" * 60)

        for feature, value in extracted_features.items():
            print(f"{feature:25} : {value}")

        print("\nFeature extraction completed successfully!")

    except Exception as error:
        print("\nError:")
        print(error)
