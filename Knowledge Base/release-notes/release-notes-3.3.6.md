# Release notes edition 3.3.6

Release date: 5 November 2024  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

# New and improved

### Dependencies

[Dependencies](../business-rules/data-dependencies.md) help you create smart, contextual field relationships in Zudello. When configured, they automatically limit the options in one field based on what you select in another. 

We now support limiting the list of available suppliers based on the subsidiary or location chosen on a document. If you choose a subsidiary or location before selecting a supplier, we can limit the list of suppliers to only those that:

- Are listed as being available for the selected subsidiary/location, or
- Have no dependency data saved (i.e. are not subsidiary/location dependent)

These dependencies will also take effect during enrichment, which is the process after document extraction where Zudello links the relevant company (supplier or customer), item, and dimension information. During enrichment, Zudello will now check:

- If there is a subsidiary and/or location set against the lines (from a keyword document coding rule or some other business rule)
- If not, if there is:
    - A default subsidiary/location set against the inbox the document was received by (emailed documents only), or
    - A default subsidiary/location set against the user who created or uploaded the document

If the above rules produce a single subsidiary/location, when linking a company we'll filter to only those companies that are:

- Listed as dependent on the subsidiary/location, or
- Listed as having no dependencies on subsidiary/location

If the above rules produce multiple subsidiaries/locations (i.e. there are different subsidiaries/locations on each line), we won't apply any filter when linking a company.

For more information, see [Dependencies](../business-rules/data-dependencies.md).

### Mileage expenses

Calculating and tracking mileage is simpler than ever with our new mileage expenses for reimbursement claims.

You can now create mileage expenses by entering the locations you've travelled to and from, and Zudello will calculate the route and distance between the two points. This distance can then be used with preset mileage rates to quickly and easily determine the value of mileage reimbursement expenses.

The new mileage expense form uses Google Maps to determine the route and distance between points. You can add multiple stops to ensure you track all required travel, without needing to process multiple mileage expenses for a single day of travel.

### Validation tolerance on forms

Validations ensure your document values are correct without the need for manual checks. Commonly used validations check for issues such as:

- Line totals that don't add up to the document subtotal or total
- Tax totals that don't match the sum of line tax amounts
- Other similar discrepancies that might indicate errors

We now support customisable tolerances on validations to account for slight rounding discrepancies and other minor differences. The default tolerance applied to all document types on Zudello V3 is $0.0201, but you can customise this for each document type in your team.

For help with adjusting the validation tolerances on your forms, please reach out to [support@zudello.com](mailto:support@zudello.com).

# Resolutions

We're constantly working to refine Zudello functionality and ensure that we address any issues as soon as possible. As part of this release, we've made the following resolutions and improvements:

- We resolved an issue where keyword coding rules weren't correctly applied due to case sensitivity. All keyword lookup rules are now case insensitive.
  
- We've restricted which modules and submodules you can select when converting a document. The following conversions are NOT allowed (structure is Existing Submodule > Converted Submodule):
    - Expenses > Mileage
    - Expenses > Claim
    - All Modules (Expenses, Sales, Purchasing, Relationships) > Requests
      
- We've improved exporting selections and filter behaviour when selecting module and submodule.
  
- We've resolved an issue with document URLs displaying incorrectly when a document was opened from the inbox. When you navigate from the inbox to a document, the URL will now refresh properly and display the URL of the document.
  
- When you're making a configuration change to dataset fields, we now display a warning and await confirmation before clearing data to prevent accidental deletes. This is in addition to the existing warning that displays when you change the dataset type.
  
- You can now view the associated tax solution on a tax rate form if the field is enabled. If you'd like to discuss enabling this field, please contact [support@zudello.com](mailto:support@zudello.com).

# Have an idea?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com). 

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.