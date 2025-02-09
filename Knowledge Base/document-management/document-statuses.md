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

| Status            | Description                                                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Scanning          | Document is being processed through optical character recognition. No user action required at this stage.                                 |
| Analysing         | Document has been flagged for system review. Automatic validation checks are being performed. No user action required at this stage.      |
| User review       | Document requires review or action before continuing. Check the document for any highlighted issues. Make corrections as needed.          |
| Ready             | Document has passed all validation checks. Ready for review and processing. You can now code and submit the document.                     |
| Reject review     | Document was rejected during approval. Review rejection comments. Make required changes and resubmit.                                     |
| Approval          | Document is with approvers. No action needed until approved or rejected. You can view the current approval step in the audit trail.       |
| Processing        | Document is moving between statuses or being sent to your external system. No user action required at this stage.                         |
| Completed         | Document has successfully processed into your external system. No further action required.                                                |
| Unable to process | Document failed to transfer to your external system. Check error messages and resolve any issues. Contact support if you need assistance. |
| Deleted           | Document has been removed from the system. No document details are retained. Cannot be reversed.                                          |
| Archived          | Document has been archived for record keeping. Document details are retained. Can be found using search and filters.                      |
| Unsupported       | Document type is not supported. Document has not been extracted. Contact support if you believe this is incorrect.                        |

### Purchase order statuses

|Status|Description|
|---|---|
|Partially received|Purchase order has been partially allocated to a receipt but not matched to an invoice. Wait for remaining goods to be received or process partial invoice matching.|
|Fully received|Purchase order has been fully allocated to a receipt but not matched to an invoice. Document is ready for invoice matching.|
|Partially invoiced|Purchase order has been partially matched to an invoice and either partially or fully matched to a receipt. Monitor for remaining invoice matching.|
|Invoiced|Purchase order has been fully matched to both an invoice and a goods receipt. No further action required.|

### Invoice matching statuses

|Status|Description|
|---|---|
|PO Missing|Invoice requires a purchase order but has no allocations to a PO. Review the invoice and either allocate it to an existing PO or create a new one.|
|GR Pending|Invoice is fully or partially allocated to a PO but requires goods receipt allocation. Check if goods have been received and process the receipt if needed.|
|PO Variance|Invoice has a discrepancy over the allowed tolerance limit. For 2-way matching, check PO allocation. For 3-way matching, verify both PO and receipt allocations.|

## Viewing document status

To check the status of your documents:

1. Open the relevant submodule
2. Look for the status name at the top of each document
3. Click the document to view more details

You can also filter documents by status to focus on specific items. For help with filtering, see [Navigating Zudello](../getting-started-with-zudello/navigating-zudello.md).

## Need help?

Contact your organisation administrator or Zudello support for assistance with document statuses and processing.