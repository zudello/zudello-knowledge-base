###### Release Date: 31st October 2024  
###### Version: v3

Here's the latest summary of what’s new and improved in Zudello, as well as what was resolved in the latest release.

# New and improved

### Bulk transaction importing

Zudello's importing feature now supports bulk transactions, allowing you to import multiple transactions at once. For more information on this feature, see [[Importing]]

### Creating Goods Receipts

We have added functionality to our goods receipting process, allowing you to choose the quantity or amount to receive when creating a new goods receipt. You can also receive all remaining quantity or amount on a purchase order by clicking **Receive all remaining**
For more information see [[Creating a Goods Receipt]]

### Price comparison alerts

In addition to comparing invoice unit prices against purchase order pricing, we have introduced the option to compare transaction unit prices to the **Purchase Price** or **Sell Price** of linked Items.

When this feature is enabled, we will compare the **Unit Price (Exclusive)** of the Transaction Line to the **Purchase Price** (Purchasing module) or **Sell Price** (Sales module) of the linked item where one exists. An icon will appear next to the **Unit Price** column to indicate whether the price matches, and you can hover over the icon for more details.
> While the Comparison is displayed next to the Unit Price, Zudello uses the **Unit Price (Exclusive)** for the comparison.  
> The comparison is calculated in the background once a transaction is saved. Consequently, comparisons may display until after you have saved the transaction.  
> Comparisons are displayed as warnings only, and cannot be used to prevent a transaction from being submitted. 

Please contact [support@zudello.com](mailto:support@zudello.com,) to discuss enabling this feature for your team.

### Expense / Claim handling improvements

We've improved several processes to reduce Expense / Claim discrepancies and improve transparency.
##### Prevent deletion of linked records

We now prevent deletion of certain records, even for users with Delete permission. The following records can no longer be deleted:
- Expenses that have been linked to a Claim
	- You need to reopen the Claim, unlink the Expense, and then you can delete the Expense
- Expenses cannot be deleted, when they have been linked to a Payment
	- You need to reopen both Expense & Payment into User Review, and unlink them via the Reconciliation Screen
- Payments that have been linked to an Expense
	- You need to reopen both Expense & Payment into User Review, and unlink them via the Reconciliation Screen

##### Restrict Users reopening completed expense transactions 

- We've introduced a new user permission called **Revert Completed** that can be used to control which users can revert or reopen transactions in a Complete type status (e.g. Completed, or custom statuses like Paid).
- If a transaction is in a Complete type status, unauthorised users will not be able to Reopen the Transaction.
- By default this permission is set to FALSE for all user groups.

##### Improve audit logs

When a Claim is submitted, the associated Expenses are set to **Closed** status. We now show an audit entry against the Expense when this status change occurs.

##### Calculate claim totals

When expenses are added, edited or removed from claims, we recalculate and refresh the Claim Lines automatically. Previously, we were relying on front end calculations to update the Claim Totals. We have now introduced backend processes that calculate the Claim Total, Tax and Subtotal

# Resolutions

### Performance improvements for approving, rejecting and force approving

We have made several performance improvements to approval-related actions. Users may notice increased speed when approving, rejecting, and force-approving documents. 

### Exporting Original Files

We've resolved an issue where files were not bulk downloading coreectly when multiple resources shared the same file name. We will now append the transaction UUID to the file name when downloading in bulk, to ensure that each file name is unique and downloaded correctly. 

### Allocations

To avoid any confusion due to the newly introduce item price comparison, we've improved the hover messaging for price comparisons when allocating transactions. We now include the Submodule name in the hover message to provide additional clarity to the comparison.

### Automation Error
An automation error was occasionally displayed in the automation log for some resources. The error did not actually cause Automations to fail, it was simply a cosmetic error that was displayed. We have now identified and resolved the root cause of the issue. 
# Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com). Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.
