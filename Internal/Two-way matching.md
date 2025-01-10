# Two-way matching

Save time and reduce errors by automatically matching each invoice to the corresponding purchase order, ensuring you only pay for what you ordered.

Two-way matching in Zudello helps you match purchase orders to invoices efficiently. This guide explains how to perform two-way matching, whether your purchase orders are created in Zudello or fetched from your ERP.

## Best practices

- Check quantities and prices match between documents
- Verify all line items are matched correctly
- Ensure any discrepancies are approved in line with your organisation's policies

## Understanding two-way matching

Two-way matching is the process of matching a purchase order to its corresponding invoice. This ensures:

- The correct items are being invoiced
- Quantities match the original order
- Prices align with agreed amounts
- Discrepancies are identified and handled appropriately

## Matching process

### Automatic matching

When an invoice is uploaded to Zudello, the system attempts to extract the purchase order number. If a valid purchase order number is found, the system automatically matches the purchase order to the invoice.

Line items are matched automatically based on either:
- Stock code
- Description
- Quantity and unit price

When using amount-based matching, line items can also be matched on an any-to-any basis. Invoice lines will be matched from top-to-bottom to any available purchase order line, until either all lines are matched or the purchase order is exhausted.
### Manual matching

If automatic matching isn't possible, you can manually match invoice lines to a purchase order:

1. Open the invoice in the Invoices 
2. Scroll down to the line items section
3. Look for orange cones indicating unmatched items
4. Enter the purchase order number
5. Review the matching results:
   - Green ticks indicate fully matched quantities
   - Green equal signs indicate fully matched prices
   - Other indicators may show partial or mismatched items

## Processing matched documents

Once matching is complete:

1. Review all line items for accuracy
2. If all quantities and prices match:
   - Click **Save and submit**
   - The invoice will flow to your ERP
3. If discrepancies exist:
   - The invoice will route through your approval flow
   - Approvers can review and confirm the differences
   - Once approved, the invoice will flow to your ERP

## Need help?

Contact your organisation administrator or Zudello support for assistance with two-way matching.