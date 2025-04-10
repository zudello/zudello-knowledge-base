# Release notes edition 3.4.3

Release date: 6 February 2025  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

## New and improved

### Invoice line consolidation

Invoice line consolidation helps simplify your document processing by combining all line items into a single consolidated line. This is particularly useful for utility bills or other invoices where detailed line items aren't necessary for your records.

We've improved the supplier and customer **Consolidate lines** option to handle invoices with repeated pricing or line items more accurately. When this option is selected, the system now creates a consolidated line with:
- Description set to **Document total**
- Quantity of **1**
- Unit price equal to the document total
- Line total equal to the document total

To improve system performance, we also now automatically consolidate lines for invoices with more than 500 lines. For these invoices, a single line is created with:
- Description set to **Document total, consolidated due to over 500 lines**
- All other values per the standard consolidate function detailed above

This new automation prevents performance issues when viewing or processing large invoices.

### Status type settings

Status type settings help maintain the integrity of your procurement workflows by controlling which actions users can take on documents at different stages of processing.

We have made a number of changes to complete-type status settings to strengthen your procurement workflows. The following restrictions now apply for all documents in a complete-type status:
- The status can't be changed using bulk actions
- Assignees can't be changed using bulk actions
- Assignees can't be changed from list or table views

These changes ensure that your completed documents maintain their integrity and align with the copies in your ERP.

### Amortisation schedules

Amortisation schedules help you track expenses that need to be spread over multiple accounting periods, ensuring accurate financial reporting.

We've added several new optional fields for amortisation scheduling against transaction lines:

- Amortisation schedule
- Amortisation start date
- Amortisation end date

These new fields allow you to record amortisation schedules directly in Zudello, eliminating the need to manually adjust these details in your ERP after completing processing in Zudello.

### Performance improvements

We continuously work to make Zudello faster and more efficient. In this release:

- We've streamlined the authentication process when you sign in and validate your permissions, making the process faster.
- We've made various other performance enhancements across the platform.

## Resolutions

We're constantly working to refine Zudello functionality and ensure that we address any issues as soon as possible. As part of this release, we've made the following resolutions and improvements:

- We've resolved an issue where large exports failed to complete.
- We've fixed an issue where dragging values (especially items or dimensions) down cells did not correctly fill.
- We've resolved an issue where the enrichment process linked the wrong item when it found both a direct SKU match and a SKU within the description.The system now gives preference to direct SKU matches over SKUs found within descriptions.
- We've resolved an issue where quotes failed to process through the enrichment process when uploaded or emailed into Zudello.

## Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Let us know at [support@zudello.com](mailto:support@zudello.com).

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.