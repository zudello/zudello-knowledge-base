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
- Purchase orders
- Goods receipts
- Invoices
- Credits

This guide references standard document statuses. For more information on statuses, see [Document statuses](../document-management/document-statuses.md)

### Quotes

The standard quote flow is:

1. A quote is uploaded and extracted
2. If the quote has passed all validation check it moves into **Ready** status; otherwise, it moves into **User Review** status
3. A user reviews the quote and makes any required changes before submitting
4. The quote is converted into a requisition

For more information on converting quotes, see [converting-a-quote-to-a-requisition-or-purchase-order](converting-a-quote-to-a-requisition-or-purchase-order.md). 

### Requisitions

The standard requisition flow is:

1. A draft requisition is created or converted from a quote
2. A user codes the requisition and submits it for approval
3. The requisition moves through the team's approval flow
4. The requisition is converted into a purchase order in **Pending** status

### Purchase orders

Purchase orders can either be:

- Created from approved requisitions, as detailed above
- Created directly as draft purchase orders

For purchase orders created from purchase requisitions, the standard flow will begin from step 4 below.

The standard purchase order flow is:

1. A draft purchase order is created
2. A user codes the purchase order and submits it for approval
3. The purchase order moves through the team's approval flow
4. Once approved, the purchase order is moved to **Pending** status
5. The purchase order is emailed to the supplier and then moved into **Placed** status
6. Placed orders are then available for two- and three-way matching matching 
7. Goods receipt matching
    - When the purchase order is partially matched to a goods receipt, the order moves to **Partially Received** status
    - When the purchase order is fully matched to a goods receipt, it moves to **Fully Received** status
8. Invoice matching
    - When the purchase order is partially matched to an invoice, the order moves to **Partially Invoiced** status
    - When the purchase order is fully matched to an invoice, it moves to **Invoiced** status
9. **Invoiced** purchase orders are no longer available for matching

Purchase orders can also be manually closed at any point. Closed purchase orders cannot be matched to receipts or invoices.

### Invoices

The standard invoice flow is:

1. An Invoice is uploaded and extracted
2. If the invoice has passed all validation check it moves into **Ready** status; otherwise, it moves into **User Review** status
3. A user codes the invoice and reviews two- and three-way matching if applicable
4. The user submits the invoice for approval 
5. The invoice moves through the team's approval flow
6. Once approved the invoice is created in your ERP
7. The invoice moves to **Completed** status
8. The statuses of any matched purchase orders are updated accordingly

### Credits

Credits are standalone documents that cannot be allocated to invoices, purchase orders, or goods receipts. In the standard flow, credits do not require approval, regardless of the total.

The standard credit flow is:

1. A credit is uploaded and extracted
2. If the credit has passed all validation check it moves into **Ready** status; otherwise, it moves into **User Review** status
3. A user reviews and codes the credit
4. The user submits the credit for processing
5. The credit is created in your ERP
6. The credit moves to **Completed** status

Credits can be related to invoices or purchase orders using the related documents and attachments feature. For more information, see [Related documents and attachments](../document-management/related-documents-and-attachments.md).

## Need help?

Contact your organisation administrator or Zudello support for assistance with purchasing flows.