# Release notes edition 3.4.2

Release date: 30 January 2025  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

## New and improved

### New feature: Keyword coding rules 

We have launched our new keyword coding rules feature, which automatically applies predefined coding when specific keywords are found on a document.

![](../images/CleanShot%202025-03-23%20at%2006.57.00@2x.png)

For more information on setting up and managing these rules, see [Keyword coding rules](../business-rules/keyword-coding-rules.md) guide.

### New Create a goods receipt feature

Goods receipts help you track when items have been received, ensuring accurate inventory management and supporting three-way matching for invoice processing.

Users now have the ability to create goods receipts directly from the related purchase order. The two documents will be automatically linked, and all header and line information can be automatically copied across. 

For more information, see our guide on [Creating a goods receipt](../purchasing-module/creating-a-goods-receipt.md).

### Editable approvals

Approval workflows help ensure the right people review and approve documents before they're processed. We've improved how editable approval milestones work to enhance system performance.

- We've implemented a new "Unlock" feature for editable milestones that makes approvals faster and more efficient
- By default, editable milestones are now read-only during the approval process
- When you need to make changes, simply click the **Unlock** button to edit the document
- After editing, you can choose to:
    - **Update** to save your changes without approving
    - **Approve** or **Reject** to complete the approval process

### Supplier and item onboarding

Managing suppliers and items efficiently is crucial for procurement processes. We've added new capabilities to streamline this process.

- You can now use computed field rules for automatically generating SKUs for items
- Default dates can now be set to "today" to better support procurement processes
    - Available as a UI setting and as a sentence action

### PDF templates

PDF templates allow you to create professional, customized documents for your business communications.

- PDF templates can now lookup additional information, including:
    - Subsidiary names
    - Document creator names
    - And more

### Allocations

Allocations help you match transaction lines to their corresponding documents, ensuring accurate records and preventing discrepancies.

- We've continued our focus on improving allocations with several enhancements:
    - Allocations are now automatically cleared when users change a document's status to **Deleted** or **Rejected**
    - Resolved an issue where allocations were not automatically created after items were linked to transaction lines
    - Improved linking between items and transactions to ensure allocations are correctly created

## Resolutions

We're constantly working to refine Zudello functionality and ensure the best possible experience. As part of this release, we've made the following performance improvements and issue resolutions:

### Performance enhancements

- Improved CPU threshold handling and scaling for better system responsiveness
- Implemented connection pooling to optimize database performance
- Enhanced our search API with dedicated resources and new options to improve search speed
- Converted more processes from asynchronous to synchronous for faster response times
- Improved auto-calculations when creating transactions, ensuring totals and tax calculate instantly when items are linked

### Issue resolutions

- Fixed an issue where users were unable to access the **Requests** submodule in **Relationships**
- Resolved an issue that prevented users from selecting fields when building exports
- Fixed display issues with logos
- Improved row selection in transaction tables, allowing highlighting with mouse for bulk duplicate and bulk delete actions
- Fixed an issue with supplier name search when configuring dependencies
- Resolved integrity issues when using the convert with duplicate function in automations
- Added a submodule filter to automations to make finding sentences for specific submodules easier
- Fixed display issues with thousand separators in table views
- Corrected the convert extension to properly reset document type selection when module or submodule changes
- Reinstated the ability to view a statement while in reconcile mode

## Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Let us know at [support@zudello.com](mailto:support@zudello.com).

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.