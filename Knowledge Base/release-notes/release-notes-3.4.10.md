# Release notes edition 3.4.10

Release date: 4 April 2025  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

## New and improved

### Enhanced security with virus scanning

Document security is essential for protecting your business data. We've introduced a new virus scanning feature powered by Clam AV that automatically checks all uploaded files for potential threats.

This new security feature:

- Automatically scans files as they're uploaded or emailed into the system
- Rejects any files that fail the security scan
- Posts warning messages in email threads when emailed attachments are rejected
- Works with manual uploads, email attachments, and files processed during splitting and merging
- Protects CSV files being uploaded for the importing tool

This enhancement helps keep your data safe while ensuring only secure files enter your system.

### Improved allocations price comparison

Allocations help you match corresponding transaction lines (e.g. purchase order lines to invoice lines), ensuring accurate records and preventing discrepancies. We've improved our price comparison feature to make it more reliable and efficient:

- The system now always compares the unit price values exclusive of tax, providing more consistent and accurate results
- We've applied a variance tolerance of 1 cent to reduce false positives
- These improvements prevent the system from flagging price differences when comparing values that are functionally the same (e.g. $39.99 vs $40.00)

This update makes the allocation process more efficient by reducing unnecessary warnings and focusing your attention only on meaningful price discrepancies.

### Budget interface improvements (Beta release)

Budgets help you track and control spending against predefined limits. We've made several visual enhancements to the budget modal to improve readability and usability:

- Improved shading to better highlight over-budget situations
- Enhanced visual distinction between remaining and processing amounts
- Negative values now appear in red for easier identification
- Various text and spelling improvements

These visual improvements make it easier to get a clear picture of your budget status at a glance.

The budgets feature currently in beta and only available for a selected number of teams. Reach out to support@zudello.com to discuss enabling this feature for your team.

## Resolutions

We're constantly working to refine Zudello functionality and ensure that we address any issues as soon as possible. As part of this release, we've made the following resolutions and improvements:

- We've resolved an issue where projects were not displayed within project task dimensions
- We've added the ability to view the **Updated by** user in the form section
- We've added additional logging to help troubleshoot any approval or automation issues that may arise

## Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Let us know at [support@zudello.com](mailto:support@zudello.com).

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.