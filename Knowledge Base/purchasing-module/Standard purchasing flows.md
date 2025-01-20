# Standard purchasing flows

Understanding how documents move through Zudello puts power back in your hands. This guide explains the standard purchasing flows in Zudello, from initial requisition through to completion, so you can accurately monitor documents from start to finish.

## Best practices

- Review and understand your organisation's document and approval workflows before processing documents
- Monitor document statuses regularly to identify any bottlenecks
- Process documents promptly to maintain efficient workflows

## Understanding the purchasing flow

This guide covers standard flows for the following document types:

- Quotes
- Requisitions
- Purchase Orders
- Invoices
- Credits

<!-- This guide references standard document statuses. For more information on statuses, see [[ Document statuses]]. -->

### Quotes

The standard quote flow is:

1. The quote is uploaded and extracted (**Scanning** status)
2. A user reviews the quote (**Ready** or **User Review** status)
3. The quote is converted into a requisition or purchase order

For more information on converting quotes, see [Converting a quote to a requisition or purchase order](Converting%20a%20quote%20to%20a%20requisition%20or%20purchase%20order.md). 

### Requisitions

The standard requisition flow is:

1. The requisition is created or converted from a quote (**Draft** status)
2. A user codes the requisition and submits it for approval
3. The requisition moves through the team's approval flow (**Approval** status)
4. The requisition is converted into a purchase order in **Pending** status

### Purchase orders

Purchase orders can either be:

- Created from approved requisitions, as detailed above
- Created directly as draft purchase orders

For purchase orders created from purchase requisitions, the standard flow will begin from step 4 below.

The standard purchase order flow is:

1. The purchase order is created (**Draft** status)
2. A user codes the purchase order and submits it for approval
3. The purchase order moves through the team's approval flow (**Approval** status)
4. Once approved, the purchase order is moved to **Pending** status
5. The purchase order is emailed to the supplier and moved to **Sent** status
6. Sent orders become available for 2- and 3-way matching matching 
7. Goods receipt matching
    - When the purchase order is partially matched to a goods receipt, the order moves to **Partially Received** status
    - When the purchase order is fully matched to a goods receipt, it moves to **Fully Received** status
8. Invoice matching
    - When the purchase order is partially matched to an invoice, the order moves to **Partially Invoiced** status
    - When the purchase order is fully matched to an invoice, it moves to **Completed** status
9. Completed purchase orders are no longer available for matching

Orders can also be manually closed at any point. Closed orders cannot be matched and won't show in available lists.

### Invoices

The standard invoice flow is:

1. An Invoice is uploaded and extracted (**Scanning** status)
2. A user codes the invoice and reviews 2- and 3-way matching if applicable (**Ready** or **User Review** status)
4. The user submits the invoice for approval 
5. The invoice moves through the team's approval flow (**Approval** status)
6. Once approved the invoice is created in your ERP
7. The invoice moves to **Completed** status

### Credits

Credits are standalone documents that cannot be allocated to invoices, purchase orders, or goods receipts. In the standard flow, credits do not require approval, regardless of the total.

The standard credit flow is:

1. A credit is uploaded and extracted (**Scanning** status)
2. A user reviews and codes the credit (**Ready** or **User Review** status)
3. The user submits the credit for processing
4. The credit is created in your ERP
5. The credit moves to **Completed** status

Credits can be related to invoices or purchase orders using the related documents and attachments feature. For more information, see [Related documents and attachments](../document-management/Related%20documents%20and%20attachments.md).

## Need help?

Contact your organisation administrator or Zudello support for assistance with purchasing flows.