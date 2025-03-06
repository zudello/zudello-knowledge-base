# Two-way matching

Only pay for what you've ordered and received, by automatically matching each invoice to both the corresponding purchase order and goods receipt. This guide explains how to review automatic three-way matching, and manually match if needed.

If you'd like to learn more about what three-way matching is and why your organisation may use it, see [Understanding two-way and three-way matching](understanding-two-way-and-three-way-matching.md).
## Best practices

- Check quantities and prices match between documents when automatically matched
- Check all line items are matched correctly
- Ensure any discrepancies are approved in line with your organisation's policies

## Automatic matching

When an invoice is uploaded to Zudello, the purchase order number will be extracted where one exists. If a purchase order with that number is found in Zudello, the system automatically matches the two documents. If a goods receipt with the number exists, or a goods receipt has been matched to the purchase order, the receipt will also be matched.

![](../images/CleanShot%202025-03-07%20at%2007.54.32@2x.png)

Each line item on the invoice is automatically matched to the corresponding lines on the purchase order and goods receipt. For quantity-based matching, common for stock invoices, matching is based on one of the following:
- Stock code
- Description
- Quantity and unit price

For amount-based matching, common for service invoices, invoice line items can be matched with the methods above. Alternatively, lines can be matched top-to-bottom to any available purchase order line, until either all lines are matched or the purchase order is exhausted.

Matching results are displayed with the following icons:
   - Green ticks indicate fully matched quantities.
   - Green equal signs indicate fully matched prices.
   - Yellow icons indicate unmatched items or price variances. You can review and action these discrepancies in line with you business's process.

![](../images/CleanShot%202025-03-07%20at%2007.25.09@2x.png)

![](../images/CleanShot%202025-03-07%20at%2007.27.02@2x.png)

![](../images/CleanShot%202025-03-07%20at%2007.30.00@2x.png)

### Manual matching

If invoice lines can't be automatically matched to purchase order lines, you can manually match them. To do so:

1. Open the invoice
2. Scroll down to the **Items** section
3. Look for icons indicating unmatched items
   ![](../images/CleanShot%202025-03-07%20at%2007.36.11@2x.png)
   
4. Click the icon on the line you'd like to match
5. The purchase order matching modal will open to the current matched purchase order
6. To match lines on the current purchase order, click **Match line** on a purchase order line
   ![](../images/CleanShot%202025-03-07%20at%2007.39.36@2x.png)
   
7. The line will automatically match with the lesser of the invoice line quantity and the remaining purchase order line quantity
8. To adjust the matched quantity, use the arrows next to the allocated quantity
   ![](../images/CleanShot%202025-03-07%20at%2007.42.50@2x.png)
   
10. To match lines on a different purchase order, click **View other purchase orders**
11. Find the relevant purchase order by scrolling or searching
 > Purchase orders will be limited to only those with the same supplier as the current invoice
12. Repeat steps 6-9
13. Click **Close**
14. Review the matching results on the invoice:
   - Green ticks indicate fully matched quantities
   - Green equal signs indicate fully matched prices
   - Yellow icons indicate remaining unmatched items or price variances

## Processing matched documents

Once matching is complete, continue processing the invoice as normal

1. Review all line items for accuracy
2. Ensure all required fields and coding are complete
3. Click **Save and submit**
4. The invoice will move through your organisation's standard document flow
   
> If you're unsure how two-way matching affects your organisation's document or approval flow, please contact your organisation administrator for more information. 

## Need help?

Contact your organisation administrator or Zudello support for assistance with two-way matching.