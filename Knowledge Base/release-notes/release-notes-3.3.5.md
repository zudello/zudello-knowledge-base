# Release notes edition 3.3.5

Release date: 31 October 2024  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

# New and improved

### Bulk transaction importing

Zudello's importing feature now supports bulk transactions, allowing you to import multiple transactions at once. For more information on this feature, see [Importing](../data-management/importing-records.md).

### Creating goods receipts

We've added functionality to simplify the goods receipting process. You can now create a goods receipt directly from a PO, and choose the quantity or amount to receive. You can also receive all remaining quantity or amount on a purchase order by clicking **Receive all remaining**.

For more information see [Creating a goods receipt](../purchasing-module/creating-a-goods-receipt.md).

### Price comparison alerts

In addition to comparing invoice unit prices against purchase order pricing, we've introduced the option to compare transaction unit prices to the purchase price or sell price of linked items.

When this feature is enabled, we'll compare the unit price (exclusive) of the transaction line to the purchase price (purchasing module) or sell price (sales module) of the linked item where one exists. An icon will appear next to the unit price column to indicate whether the price matches. You can hover over the icon for more details on the comparison.

Zudello uses the tax exclusive unit price for the comparison, regardless of whether the unit price on the invoice is tax inclusive or exclusive. 

The comparison is calculated in the background once you save a transaction. Consequently, comparisons may not display until after you've saved the transaction.

Comparisons are displayed as warnings only and can't be used to prevent a transaction from being submitted.

Please contact [support@zudello.com](mailto:support@zudello.com) to discuss enabling this feature for your team.

### Expense/claim handling improvements

We've improved several processes to reduce expense/claim discrepancies and improve transparency.

#### Prevent deletion of linked records

We now prevent deletion of certain records, even for users with delete permission. The following records can no longer be deleted:

- Expenses that have been linked to a claim
    - You need to reopen the claim, unlink the expense, and then delete the expense
- Expenses that have been linked to a payment
    - You need to reopen both the expense and the payment into **User Review** status, and unlink them via the reconciliation screen
- Payments that have been linked to an expense
    - You need to reopen both the expense and the payment into **User Review** Status, and unlink them via the reconciliation screen

#### Restrict users reopening completed expense transactions

We've introduced a new user permission called **Revert completed**. Only users with this permission enabled can revert or reopen transactions in a complete-type status (e.g. **Completed**).

By default, this permission is disabled for all user groups.

#### Improve audit logs

When a claim is submitted, the associated expenses are set to **Closed** status. We now show an audit log entry against the expense when this status change occurs.

#### Calculate claim totals

When expenses are added, edited, or removed from claims, we recalculate and refresh the claim lines automatically. Previously, we relied on front end calculations to update the claim totals. We've now introduced backend processes that calculate the claim total, tax, and subtotal. This ensure that the claim totals are always kept up-to-date and correct. 

# Resolutions

### Performance improvements for approving, rejecting, and force approving

We've made several performance improvements to approval-related actions. You may notice increased speed when approving, rejecting, and force approving documents.

### Exporting original files

We've resolved an issue where files weren't bulk downloading correctly when multiple resources shared the same file name. We now append the transaction UUID to the file name when downloading in bulk to ensure that each file name is unique and downloaded correctly.

### Allocation messaging

To avoid any confusion around the newly introduced item price comparison, we've improved the hover messaging for price comparisons when allocating transactions. We now include the submodule name in the hover message to provide additional clarity to the comparison.

E.g. Purchase order price comparison displayed on an invoice
![](../images/Pasted%20image%2020250312114815.png)

E.g. Receipt price compaison displayed on an invoice
![](../images/Pasted%20image%2020250312114741.png)

### Automation error

An automation error was occasionally displayed in the automation log for some resources. The error was not caused by or the cause of an automation failure; it was simply a cosmetic error that was displayed. We've now identified and resolved the root cause of the issue.

# Have some ideas?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com).

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone. 