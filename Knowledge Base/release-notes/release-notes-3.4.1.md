# Release notes edition 3.4.1

Release date: 16 January 2024  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

## New and improved

### Allocations

Allocations help you match transaction lines to their corresponding documents, ensuring accurate records and preventing discrepancies. We've continued our focus on allocations and introduced the following improvements:

- Allocations are now automatically cleared when you change a document type in a way that affects matching requirements. This prevents confusion and ensures your allocations remain accurate when:
    - Changing from [three-way matching](../purchasing-module/three-way-matching.md) to [two-way matching](../purchasing-module/two-way-matching.md) document types
    - Changing between quantity-based and amount-based allocation document types
    - Changing to a document type that doesn't require allocations

When these changes occur, Zudello will display a warning and ask for your confirmation before clearing the allocations. If allocations are still required after the change, remaining and discrepancy

![](../images/CleanShot%202025-04-08%20at%2013.29.29.png)

### Duplicate checking validation

Zudello helps prevent unnecessary work and overpayments through automated duplicate checking. We've improved our duplicate detection to better protect your business from processing the same document multiple times:

- Duplicate checks now verify that each combination of submodule, supplier/customer, and document number is unique
- Duplicate checks run automatically when you open a document and when you edit the supplier or document number
- Duplicates are now treated as blocking errors if the document number field is visible and required, preventing submission until the issue is resolved
- If the document number is not marked as required, duplicate checks will appear as warnings only

These enhancements provide stronger protection against duplicate payments while maintaining flexibility when you need it.

### Supplier and customer specific pricing

Price comparisons help you quickly identify pricing discrepancies across your transactions. We've expanded our price comparison options to give you more flexibility.

#### Customer/supplier specific pricing

Unit prices are now compared to pricing set in the item alternative table for the relevant supplier (purchasing module) or customer (sales module).

- When specific pricing is available in the item alternatives table, an indicator appears next to the unit price
- If no specific price is available, the system falls back to comparing against the purchase price, sell price, or retail price

#### Auto-fill pricing

When creating requisitions, Zudello can now automatically fill in customer or supplier specific pricing, ensuring that you and your customers always pay the right price.

When a supplier (purchasing module) or customer (sales module) is assigned to the transaction, selecting an item from the catalogue will automatically fill the unit price with pricing from the item alternatives table.

### Group membership management

User groups help you manage permissions and access for teams of users. We've introduced a new **Group Membership Management** page to make it easier to view and manage which users belong to specific groups.

![](../images/CleanShot%202025-04-08%20at%2013.45.47%201.png)

Organisation administrators can now access a central location to view and manage user group associations across teams. The page displays all user groups in a table format, with key information such as:
- Group name and description
- Group type (indicated by colour)
- Number of associated users
- Expandable list of users for each group

You can also filter for a specific team to view all users associated with the user groups for that team. Collapse all and expand all shortcuts make navigation easier, while search functionality helps you quickly locate specific user groups, user names, or email addresses. 

The add users button allows you to quickly add multiple users to a group. 

![](../images/CleanShot%202025-04-08%20at%2013.43.22.png)

This new management page helps ensure your user group membership remains up to date and in line with your organisation's needs. For more information, see [User groups](../user-management-and-security/user-groups.md). 

## Resolutions

We're constantly working to refine Zudello functionality and ensure that we address any issues as soon as possible. As part of this release, we've made the following resolutions and improvements:

- Several performance improvements have been implemented across the platform, including a specific performance issue that affected dependency deletion
  
- We've fixed authentication issues related to Microsoft Entra ID (formerly Azure AD)
  
- We've resolved a MIME type issue that prevented certain documents from being uploaded
  
- Unit price exclusive calculations now work correctly when quantities are negative
  
- Unclassified documents are now rescanned automatically once you classify them
  
- The tax included flag is now set correctly when documents don't have a subtotal
  
- We've added a new payment reference field for suppliers, customers, and employees
  
- Delivery addresses are no longer overwritten when converting quotes to purchase orders

## Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Let us know at [support@zudello.com](mailto:support@zudello.com).

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.