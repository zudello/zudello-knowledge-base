# Release notes edition 3.3.7

Release date: 11 November 2024  
Version: v3

Here's the latest summary of what's new and improved in Zudello, as well as what we resolved in the latest release.

# New and improved

### Enhanced approval routing options

Zudello's approval system routes documents to the right people at the right time, helping you maintain compliance and control over your business processes. Our delegation of authority (DOA) features ensure that approvals follow your company's governance requirements.

We've expanded our approval routing options to handle more complex approval scenarios:

- **Exclude submitters from approval flows**: You can now configure approval flows to automatically exclude document submitters from the approval process. This improves separation of duties by ensuring that the person who submits a document can't also approve it, even if they would normally be part of the approval flow.
    
- **Enhanced approval routing methods**: We've refined how approval flows work when submitters are excluded:
    
    - **Start from bottom**: Follows your defined DOA from the lowest approval level upward
    - **Start from submitter**: Begins the approval process from the submitter of the document
    - **User with sufficient limit**: Routes directly to the first approver with a sufficient approval limit 

These enhancements help you meet compliance requirements while maintaining efficiency and  simplicity within your approval flow.

# Resolutions

### Approval sentence handling

We've resolved an issue where error messages were sometimes displayed unnecessarily during the approval process. Previously, when certain approval conditions weren't met and the system was configured to skip that step, an error message would still appear in the system logs.

We've improved this process to display appropriate messages based on your exception handling configuration:

- **Fail if no match**: If a required condition isn't met, the system will stop processing and display an error message
- **Skip sentence if no match**: If a condition isn't met, the system will skip that automation and proceed to the next automation without unnecessary error messages
- **Skip line if no match**: The system will only process document lines that meet the specified conditions

These improvements provide clearer information about approval routing decisions and reduce unnecessary error messages.

# Have some ideas?

Do you have an idea for a new feature or how we can improve our current features? Please let us know at [support@zudello.com](mailto:support@zudello.com).

Your ideas and feedback are an important part of our product planning process to make Zudello better for everyone.