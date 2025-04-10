# Release notes edition 3.4.8

Release date: 20 March 2025  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

## New and improved

### Improved catalogue search

Finding the right items in your catalogue is essential for efficient document processing. We've made significant improvements to how searching works when looking for items by SKU or description.

#### Within the catalogue submodule

We now use the following conditions for searches within the catalogue submodule:

- For searches with hyphens (e.g. C-2500-NAVY-87R) we look for an exact string match 
- When you enter multiple keywords separated by spaces (e. g. Yakka Cargo), both keywords must be present in the results
- Results that exactly match your search criteria now appear at the top of your results, with partial matches displayed further down the list
- Sorting order is maintained based on the view you're using (date updated or date created)

#### In drop-down selectors:

- Item selection drop-downs, such as on transactions and other forms, now show results ordered by relevance
- The most relevant matches appear at the top of the list

These improvements make it much easier to find exactly what you're looking for, saving you time when creating and processing documents.

### Keyword coding enhancements

[Keyword coding rules](../business-rules/keyword-coding-rules.md) help automate the coding of dimensions and other information on your transactions. We've updated how these rules work to give you more control:

- Rules now fully overwrite fields rather than only filling in blank values
- All configured rules are now executed in the order they appear in the rules list
- If multiple rules apply to the same field, the last rule executed will determine the final value

This change gives you more flexibility when setting up complex coding rules, as you can now create layered rules that run one after the other.

### Expanded fields for delegation of authority (DOA) approvals

Delegation of authority (DOA) rules ensure that transactions are approved by the right people, every time. We've expanded our DOA capabilities to include the following new dimensions:

- Item groups
- Item categories
- Project types 
- Project groups

This expansion gives you more flexibility when configuring approval workflows, allowing you to match your ZUdello workflow exactly to your business needs. 

### Place order audit improvements

Purchase order management helps you track orders with suppliers throughout the full procurement cycle. To maintain accurate audit trails, we've made the following improvement to system behaviour.

When duplicating a purchase order, the **Placed by** and **Placed at** fields are now automatically cleared. This ensures that your audit trails remain accurate and reliable, making it clear which orders have been placed, when they were placed, and by whom.

## Resolutions

We're constantly working to refine Zudello functionality and ensure that we address any issues as soon as possible. As part of this release, we've made the following resolutions and improvements:

- We've implemented an automatic retry system for PDF generation to ensure reliability even during temporary service interruptions
- We've optimised timezone settings for UK customers to improve performance
- We've made improvements to the saving process for user groups with numerous permissions
- We've resolved an issue where the **Created by** user field couldn't be added to forms, complementing the previously released ability to add **Placed by** and **Submitted by** fields

## Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Let us know at [support@zudello.com](mailto:support@zudello.com).

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.