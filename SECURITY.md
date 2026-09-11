# Security

This repository is an unofficial, read-only community integration for the MOVAhome cloud.

## Do not post credentials

Never include any of the following in a GitHub issue, pull request, screenshot, log, or diagnostic file:

- MOVAhome email address or password
- access or refresh tokens
- cookies or authorization headers
- personal device identifiers
- Home Assistant `.storage` files

If you accidentally publish credentials or a token, remove the material and rotate the affected credentials immediately.

## Read-only scope

The public integration intentionally uses property reads only. It does not include the experimental battery-write/controller code used during private interoperability testing.

## Reporting a security concern

Until a dedicated security contact is published, do not open a public issue containing sensitive details. Use GitHub's private security-advisory flow once it is enabled for the repository.

## Application protocol constants

The cloud client contains application-level constants observed during interoperability testing that are required for the tested MOVAhome login flow. They are not user-specific account credentials. No user-specific credentials are committed to this repository.
