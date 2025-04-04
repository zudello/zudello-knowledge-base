# Release notes edition 3.3.8

Release date: 20 November 2024  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

# New and improved

### Document type default statuses

Document types now have configurable default statuses that are applied when documents are created or reopened:
    - Transactions (invoices, purchase orders, etc.) default to **Review** status when created and **Ready** status when reopened
    - Non-transactions (items, suppliers, customers, dimensions) default to **Active** status for both creation and reopening

You can customise these settings in the document type settings.

### Auto-approve for submitters

Previously, if document submitters were also valid approvers on a document, they would need to reopen and approve documents they had already submitted for approval. 

You can now configure approval flows to automatically approve any steps for document submitters, streamlining the approval process and removing the need for double handling. 

## New LLM document extraction pipeline

Zudello's document extraction system pulls key information from your documents and makes it available for processing.

All teams are now automatically opted into our LLM (Large Language Model) extraction pipeline, which provides faster and more accurate document extraction. This advanced technology significantly improves the quality and speed of information extracted from your documents.

### Performance enhancements

We've made several improvements to Zudello's performance, helping you work faster and more efficiently:

- **Faster document enrichment and allocations**: We've streamlined how documents are processed during enrichment, reducing the time it takes to extract and code your documents. We've also optimised how we calculate allocation variances, making the matching process faster.
  
- **Improved transaction loading**: Opening transactions with allocations is now faster, as we've reduced the amount of background information loaded when viewing these documents.
  
- **Faster claim processing**: Processing claims with multiple linked expenses is now significantly faster. We've reduced processing time for claims with 20-30 linked expenses from nearly 2 minutes down to about 45 seconds.

We're committed to ongoing performance improvements and will continue to make Zudello faster with each release.

# Resolutions

### Bank account and ABN validations 

- We've resolved an issue where bank account and ABN validations were sometimes appearing when they shouldn't. Validations now properly respect their document type extension settings.
  
- We've corrected calculations for amount-based matching, ensuring that matching status and variance percentages are displayed accurately.

- We've resolved an issue where users couldn't complete transactions with lengthy address information.
  
- We've added search functionality to the [keyword coding](../business-rules/keyword-coding-rules.md) page, making it easier to find and work with document coding settings.
  
- We've upgraded several front-end components to ensure ongoing compliance with security standards.

# Have some ideas?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com). Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.