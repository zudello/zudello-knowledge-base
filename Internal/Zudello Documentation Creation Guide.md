## Overview
This guide outlines the step-by-step process for creating high-quality documentation for Zudello software products. By following these steps, you'll ensure consistent, clear, and useful documentation that meets our standards.

## Prerequisites
- Loom screen recording software
- Access to Anthropic Claude
- Markdown editor (e.g. Obsidian)
- Access to Zudello software

## Step 1: Recording the Process

### Recording Setup
1. Open Loom and ensure your microphone is working
2. Set up your screen for recording:
   - Clear unnecessary windows and notifications
   - Prepare Zudello software in the correct starting state
   - Close sensitive or irrelevant applications

### Recording Best Practices
1. Speak clearly and at a moderate pace
2. Follow a logical sequence of actions
3. Pause briefly between major steps
4. Highlight important UI elements or actions
5. Mention any prerequisites or assumptions
6. Include common variations or alternative paths

### Recording the Content
1. Start Loom recording
2. Introduce the topic briefly
3. Demonstrate the process step-by-step
4. Show error states and recovery steps if applicable
5. Conclude with a summary
6. Stop the recording

## Step 2: Obtaining the Transcript

### Accessing the Transcript
1. Open your recording in Loom
2. Navigate to the transcript section
3. Click "Copy transcript" or equivalent option
4. Save the transcript in a temporary document

### Transcript Cleanup
1. Review for obvious transcription errors
2. Add paragraph breaks for major sections
3. Note timestamps of important moments
4. Mark sections that need special attention

## Step 3: Creating the Initial Prompt

### Prompt Structure
```markdown
Please help me create technical documentation based on the following Loom recording transcript. Follow these guidelines:

1. Style and Format:
   - Follow the Zudello Writing Guide provided below
   - Match the style of the example article
   - Use clear, concise technical writing
   - Include proper headings and sections

2. Content Requirements:
   - Start with a clear overview
   - Break down steps logically
   - Include prerequisites
   - Add troubleshooting sections
   - Note important warnings or tips

3. Additional Context:
   [Add any specific requirements or context]

Here are the reference materials:

<zudello_writing_guide>
[WRITING_GUIDE_PLACEHOLDER]
</zudello_writing_guide>

<example_article>
[EXAMPLE_ARTICLE_PLACEHOLDER]
</example_article>

Transcript:
[PASTE_TRANSCRIPT_HERE]
```

## Step 4: Using Claude to Generate Documentation

### Setup
1. Open Claude (Anthropic Console)
2. Create a new conversation
3. Prepare your materials:
   - Crafted prompt
   - Cleaned transcript
   - Writing guide
   - Example article

### Input Process
1. Paste the complete prompt
2. Add the transcript
3. Include the writing guide
4. Add the example article
5. Review for formatting before sending

### Working with Claude
1. Review initial output
2. Ask for clarifications if needed
3. Request specific revisions
4. Save all versions for comparison

## Step 5: Editing the Generated Content

### Initial Review
1. Copy Claude's output to your Markdown editor
2. Check for:
   - Structural integrity
   - Logical flow
   - Missing steps
   - Technical accuracy
   - Formatting issues

### Content Enhancement
1. Add missing context
2. Clarify ambiguous instructions
3. Expand troubleshooting sections
4. Insert relevant screenshots
5. Add cross-references
6. Include warning boxes

### Style Alignment
1. Check against Writing Guide
2. Compare with example article
3. Standardize terminology
4. Adjust tone and voice
5. Format for consistency

## Step 6: Prompt Refinement

### Comparison Analysis
1. Create a side-by-side comparison:
   - Original Claude output
   - Your edited version
2. Identify major differences:
   - Structure changes
   - Content additions
   - Style adjustments
   - Format improvements

### Feedback Collection
Prompt for Claude:
```markdown
I have two versions of documentation for comparison:

1. Original (Claude-generated):
[Insert original version]

2. Final (Edited):
[Insert edited version]

Please analyze:
1. Key differences between versions
2. What was missing from the original
3. How to modify the initial prompt to get closer to the final version
4. Specific prompt improvements for future use
```

### Prompt Improvement
1. Document Claude's suggestions
2. Update your prompt template
3. Test new prompt with another document
4. Iterate and refine

## Best Practices

### Documentation Quality
- Ensure all steps are complete and accurate
- Include realistic examples
- Add context for complex steps
- Cross-reference related documentation
- Use consistent formatting

### Process Efficiency
- Save prompt templates
- Create reusable sections
- Document common adjustments
- Build a feedback loop
- Track improvements over time

### Common Pitfalls to Avoid
- Skipping the transcript cleanup
- Rushing the editing phase
- Ignoring style guidelines
- Forgetting prerequisites
- Omitting troubleshooting sections

## Quality Checklist

Before Finalizing:
- [ ] All steps are clear and complete
- [ ] Prerequisites are listed
- [ ] Screenshots are relevant and clear
- [ ] Troubleshooting is included
- [ ] Style matches guidelines
- [ ] Format is consistent
- [ ] Technical terms are explained
- [ ] Links are working
- [ ] Cross-references are accurate
- [ ] Warnings are prominent

## Template Library

### Basic Article Template
```markdown
# [Feature/Process Name]

## Overview
[Brief description of the feature or process]

## Prerequisites
- [Required access or permissions]
- [Required software or tools]
- [Required knowledge]

## Process
1. [Step One]
   - [Details]
   - [Screenshots]

2. [Step Two]
   - [Details]
   - [Screenshots]

## Troubleshooting
### Common Issue 1
- Problem: [Description]
- Solution: [Steps to resolve]

### Common Issue 2
- Problem: [Description]
- Solution: [Steps to resolve]

## Related Resources
- [Link to related documentation]
- [Link to support resources]
```

## Conclusion
Follow this guide to create consistent, high-quality documentation for Zudello products. Remember to iterate and improve your process based on feedback and experience.