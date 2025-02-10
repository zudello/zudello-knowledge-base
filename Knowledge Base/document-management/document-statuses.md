# Document statuses

Zudello uses document statuses to track documents as they move through your business processes. Understanding these statuses will help you quickly identify where documents are in their lifecycle and what actions you need to take.

## Best practices

To effectively manage documents in your workflows:

- Check document statuses regularly to identify items needing attention
- Action documents in review statuses promptly to maintain efficient process flow
- Review rejected documents to identify any common issues

## Understanding document statuses

Zudello uses the standard statuses below to represent where documents are in their lifecycle. Your team may have additional custom statuses to support specific workflow requirements.

### General processing statuses

| Status            | Description                                                                                                                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scanning          | Document is being extracted. No user action required at this stage.                                                                                                                           |
| Ready             | Document has passed all validation checks. You can now code and submit the document.                                                                                                          |
| User Review       | Document has failed one or more validation checks. Check the document for any highlighted issues, then code and submit the document.                                                          |
| Reject Review     | Document was rejected during approval. Review rejection comments, make required changes and resubmit.                                                                                         |
| Approval          | Document is awaiting approval. Action is required from the approver/s shown under the current approval step.                                                                                  |
| Processing        | Document is moving between statuses or being sent to your ERP. No user action required at this stage.                                                                                         |
| Completed         | Document has successfully processed to your ERP. No further action required.                                                                                                                  |
| Unable to Process | Document failed to transfer to your ERP. Review error messages and resolve any issues. Contact support if you need assistance.                                                                |
| Deleted           | Document has been deleted. The document can still be opened and reviewed for audit purposes.                                                                                                  |
| Archived          | Document has been archived. Document details remain unchanged, but the document will not move through any further workflow. The document can still be opened and reviewed for audit purposes. |
| Unsupported       | Document type is not supported. Document has not been extracted.                                                                                                                              |

### Purchase order specific statuses

| Status             | Description                                                                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Partially Received | The purchase order has been partially allocated to a receipt, but not matched to an invoice. The purchase order is available for remaining receipt matching and invoice matching. |
| Fully Received     | The purchase order has been fully allocated to a receipt, but not matched to an invoice. The purchase order is available for invoice matching.                                    |
| Partially Invoiced | The purchase order has been partially matched to an invoice, and either partially or fully matched to a receipt. The purchase order is available for invoice matching.            |
| Invoiced           | The purchase order has been fully matched to both an invoice and a goods receipt. No further action required.                                                                     |

### Invoice specific statuses

| Status      | Description                                                                                                                                                                                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PO Missing  | The invoice requires a purchase order, but has no allocations to a purchase order. Review the invoice and allocate it to an approved purchase order.                                                                                                        |
| GR Pending  | The invoice is fully or partially allocated to a purchase order, but has no allocations to a goods receipt. Check if goods have been received and match a goods receipt when available.                                                                     |
| PO Variance | The invoice has a discrepancy over the allowed tolerance, and requires further approval. For 2-way matching, check the purchase order allocation before approving. For 3-way matching, verify both purchase order and receipt allocations before approving. |
> Contact your organisation administrator to check your team's allowed discrepancy tolerance

## Viewing document status

Documents under each submodule are grouped by status. The status name and colour are displayed at the top of each grouping. 

To show or hide document statuses:

1. Open the relevant submodule
2. Click **Status**
3. Select the statuses you would like to view from the drop-down
4. Click **Done**

## Need help?

Contact your organisation administrator or Zudello support for assistance with document statuses and processing.