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

### Quotes

The lifecycle of a quote is:

1. The quote is uploaded 
2. Once extracted, the quote is reviewed
3. The quote is converted into a requisition or purchase order

For more information on converting quotes, see [[Converting documents in Zudello]]

### Requisitions

The standard requisition flow is:

1. The requisition is created in **Draft** status
2. Once populated, it is submitted for approval
3. Once approved, the requisition is converted into a purchase order
4. The purchase order is moved to **Pending** status to indicate that is ready to be sent to the supplier

### Purchase orders

Purchase orders can either be:

- Created from approved requisitions
- Created directly as draft purchase orders

For purchase orders created from purchase requisitions, the standard flow will begin from step 4 below.

The standard purchase order flow is:

1.  The purchase order is created in **Draft** status
2. Once populated, it is submitted for approval
3. Once approved it moves to **Pending** status, indicating the order is ready to be sent to the supplier
5. The purchase order is emailed to the supplier and moves to **Sent** status
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

1. An Invoice is uploaded to the system in **Scanning** status
2. If the invoice passes all validations, it moves to **Ready** status
   or
   If the invoice fails one or more validations, it moves to **User Review** status
4. A user reviews and codes the invoice, including 2- or 3-way matching if applicable
5. The invoice is submitted for approval
6. Once approved the invoice is created in your ERP
7. The invoice moves to **Completed** status

### Credits

Credits are standalone documents that cannot be allocated to invoices, purchase orders, or goods receipts. In the standard flow, credits do not require approval regardless of amount.

The standard credit flows is:

1. A credit is uploaded to the system in **Scanning** status
2. If the credit passes all validations, it moves to **Ready** status
   or
   If the credit fails one or more validations, it moves to **User Review** status
4. A user reviews and codes the credit
5. The invoice is submitted for processing
6. The credit is created in your ERP
7. The credit moves to **Completed** status

Credit notes can be related to invoices or purchase orders using the related documents and attachments feature. For more information, see [[Related documents and attachments]].

## Need help?

Contact your organisation administrator or Zudello support for assistance with purchasing flows.