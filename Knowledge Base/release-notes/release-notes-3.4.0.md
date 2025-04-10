# Release notes edition 3.4.0

Release date: 8 January 2025  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

# New and improved

### Approvals

#### Start from submitter for user group DOAs

We’ve expanded the functionality for delegation of authority (DOA) approvals by introducing the ability to start approvals from the submitter. This gives you greater flexibility, allowing approvals to be triggered based on the user who submits the transaction.

Previously, only the **Start from bottom** option worked for user group DOAs. We now support the **Start from submitter** logic, which checks if the submitter is a member of any applicable groups in the DOA and begins the approval process from there. If the submitter is not part of any group, the system will revert to the **Start from bottom** behaviour to avoid errors.

This change ensures that the approval process is more dynamic, and avoids submitters having to reapprove documents that they submitted. 

#### Exclude submitter logic for user group DOAs

We’ve introduced improvements to prevent approvals from getting stuck when the submitter is not able to approve their own documents.

The system will now ensure that no approval steps are created where the only approver is the submitter. If the submitter is part of a group with only one member, the approval process will skip this milestone and move to the next applicable step.

#### Multi-select user groups for DOA approvals

You can now select multiple user groups as the approvers for a single approval step, providing more flexibility in how the approval process is configured.

### Transaction header and related models in DOA approvals

We’ve expanded DOA support to include transaction header and related dimensions, giving you more flexibility when setting up and managing approvals.

Previously, DOAs could only be configured with transaction line dimensions. Now, you can configure DOAs using header dimensions (such as supplier or customers) and related dimensions (such as account group). 

This provides further flexibility in the approval process, to ensure your documents are approved by the right person every time.

### Importing

Zudello's importing feature let's you efficiently create new records or update existing ones in bulk, giving you more control over your team's data.

We have now added the ability to import inventory receipts, making it easier to process large volumes of inventory transactions.

We have removed the ability to import mileage expenses. Mileage expenses need to be entered via the expenses module, to ensure that all necessary information is captured. 

# Resolutions

- We’ve resolved an issue where dependencies weren’t automatically deleted when related values were deleted. Now, deleting a record will properly remove any related dependency on other records.
- An issue that prevented users from duplicating a Sales Order into a Purchase Order has been fixed.
- We’ve fixed an error where some table views would fail to load, improving overall stability and performance.
- An issue with audit logs displaying dimension UUIDs instead of names has been resolved, making logs easier to read.
- We’ve continued our work on improving system performance, including converting more endpoints from asynchronous to synchronous processing.

# Have some ideas?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com).

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.