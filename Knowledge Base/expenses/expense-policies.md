# Expense policies

Zudello's expense policies feature helps your organisation enforce spending rules, ensure compliance, and streamline the expense approval process. This guide explains how expense policies work in Zudello and how they help maintain financial control while simplifying the reimbursement process for everyone.

## Understanding expense policies

Expense policies are a set of rules that define what business expenses are acceptable and how they should be processed. They help:

- Ensure consistent handling of expenses across your organisation
- Highlight potential policy breaches automatically
- Prevent back-and-forth between approvers and submitters

## How policies work in Zudello

Expense policies use Zudello's natural language engine rules that are easy to configure and understand. Policies are automatically evaluated at key points in the expense process:

- When an expense is saved
- When an expense is validated
- When an expense is added to a claim
- When a claim is submitted for approval

### Policy types

Zudello supports various policy types to accommodate different business requirements:

#### Date checks

Date checks validate that expenses are submitted within acceptable timeframes. A common example is:

- Claims must be submitted within 60 days of incurring the expense

#### Value checks

Value checks compare expense amounts against predefined limits. Common examples include:

- Maximum meal expense per person
- Maximum gift amount per financial year

#### Attachment checks

Attachment checks ensure required documentation is provided. Common examples include enforcing one of the following attachments:

- Proof of purchase receipts
- Travel itineraries
- Supporting documentation for specific expense types

#### Keyword checks

Keyword checks compare values in specific transaction fields against a list of keywords. Common examples include:

- Identifying non-reimbursable items like alcohol
- Flagging specific expense categories for additional review

#### Field checks

Field checks ensure all required information has been provided. Common examples include:

- Attendee information for meal expenses
- Business purpose justification
- Type of spend (personal spend vs card spend)

## Policy outcomes

When a policy check runs, it can produce different outcomes based on your configuration:

### Warnings

Warnings display notifications to submitters without blocking the process. Examples include:

- "Claims should be made within 60 days of incurring the expense, please be more timely with your submission in the future."
- "This amount exceeds the recommended limit for this expense type, and will require additional approval."

### Blocking errors

Blocking errors prevent users from proceeding until the issue is resolved. Examples include:

- "Please provide the names of all attendees."
- "Please attach your travel itinerary."

### Alerts

Alerts display information to approvers that may not be shown to submitters. For example:

- "This user has submitted five out-of-policy claims in the past three months."

## What's next?

Expense policies are a powerful tool in automating your expense processing and giving time back to users across your business. Please reach out to support@zudello.com to discuss enabling expense policies for your team. 

For more information on working with expenses, see these related articles:

- [Expense types](expense-types.md)
- [Uploading expenses](uploading-expenses.md)
- [Coding and validating expenses](coding-and-validating-expenses.md)
- [Submitting a claim](submitting-a-claim.md)
- [Approving claims](approving-claims.md)