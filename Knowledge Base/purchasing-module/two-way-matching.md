# Two-way matching

Save time and reduce errors by automatically matching each invoice to the corresponding purchase order, ensuring you only pay for what you ordered. This guide explains how to review automatic two-way matching, and manually match if needed.

If you'd like to learn more about what two-way matching is and why your organisation may use it, see [Understanding two-way and three-way matching](understanding-two-way-and-three-way-matching.md).

## Best practices

- Check quantities and prices match between documents when automatically matched
- Check all line items are matched correctly
- Ensure any discrepancies are approved in line with your organisation's policies

## Quantity-based matching vs amount-based matching

Zudello supports two approaches to matching invoice lines to purchase order lines:

- Quantity-based matching compares specific quantities across documents, ensuring the exact number of units are reflected in purchase orders and invoices. 
	- For example, when ordering 20 software licences at $150 each, quantity-based matching verifies are being billed for the correct number of licences, even if there is a change in price.

- Amount-based matching focuses on comparing monetary values across documents, and "draws down" on the approved amount until the purchase order is exhausted. 
	- For example, when ordering consulting services for $5,000, amount-based matching ensures the total invoiced amount doesn't exceed the approved purchase order value, regardless of how the amount is split between invoices.

## Automatic matching

When an invoice is uploaded to Zudello, the purchase order number will be extracted where one exists. If a purchase order with that number is found in Zudello, the system automatically matches the two documents.

![](../images/CleanShot%202025-04-04%20at%2008.41.38.png)

Each line item on the invoice is automatically matched to the corresponding line on the purchase order. For quantity-based matching, common for stock invoices, matching is based on one of the following:
- Stock code
- Description
- Quantity and unit price

For amount-based matching, common for service invoices, invoice line items can be matched with the methods above. Alternatively, lines can be matched top-to-bottom to any available purchase order line, until either all lines are matched or the purchase order is exhausted.

Matching results are displayed with the following icons:

| Icon                                                         | Matched status                                                                           |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| ![](../images/CleanShot%202025-04-04%20at%2009.20.31@2x.jpg) | Fully matched                                                                            |
| ![](../images/rrrrrrrrrr%201.jpg)                            | Partially matched; the number indicates the missing quantity                             |
| ![](../images/bgerwqrwfrgfwrq3frgf.jpg)                      | Line not matched                                                                         |
| ![](../images/Untitled.jpg)                                  | The price of the matched transactions matches the price of the current transaction       |
| ![](../images/CleanShot%202025-04-04%20at%2009.31.57@2x.jpg) | The price of the matched transaction is higher than the price of the current transaction |
| ![](../images/CleanShot%202025-04-04%20at%2009.31.42@2x.jpg) | The price of the matched transaction is lower than the price of the current transaction  |
| ![](../images/CleanShot%202025-04-04%20at%2009.38.34@2x.jpg) | Multiple icons appear if you are matching to multiple transactions                       |


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
6. To match lines on the current purchase order, click **Match line** 
![](../images/CleanShot%202025-03-07%20at%2007.39.36@2x.png)
   
7. The line will automatically match with the lesser of the invoice line quantity and the remaining purchase order line quantity
8. To adjust the matched quantity, use the arrows next to the allocated quantity
![](../images/CleanShot%202025-03-07%20at%2007.42.50@2x.png)

9. To match lines on a different purchase order, click **View other purchase orders** 
10. Find the relevant purchase order by scrolling or searching
 > Purchase orders will be limited to only those with the same supplier as the current invoice
11. Repeat steps 6-8
12. Click **Close**
13. Review the matching results on the invoice:
   - Green ticks indicate fully matched quantities
   - Green equal signs indicate fully matched prices
   - Yellow icons indicate remaining unmatched items or price variances

## Reviewing and editing matching

To review and edit existing matching, click the expand icon at the start of a line.

![](../images/CleanShot%202025-03-09%20at%2009.20.25@2x.png)

This will show the purchase order to the line, including the allocated quantity and price. Click the **Document #** to open the related purchase order.

To edit existing matching, click the edit icon next to **Purchase Order**. This will open the matching modal, and you can follow the steps for manual matching above. 

## Processing matched documents

Once matching is complete, continue processing the invoice as normal

1. Review all line items for accuracy
2. Ensure all required fields and coding are complete
3. Click **Save and submit**
4. The invoice will move through your organisation's standard document flow
   
> If you're unsure how two-way matching affects your organisation's document or approval flow, please contact your organisation administrator for more information. 

## Need help?

Contact your organisation administrator or Zudello support for assistance with two-way matching.