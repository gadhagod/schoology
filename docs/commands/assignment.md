### assignment
Get assignment data.

**Syntax** \
`schoology assignment [OPTIONS]`

**Options** 
- `--section-id TEXT`
 - Assignment section ID
 - Required
- `--assignment-id TEXT`
 - Assigment ID
 - Required
- `--title`
 - Show title
 - Not required
- `--description`
 - Show description
 - Not required
- `--due-date`
 - Show due date
 - Not required
- `--weight`
 - Show grade weight
 - Not required
- `--folder`
 - Show folder ID
 - Not required
- `--last-updated`
 - Show time last updated
 - Not required
- `--completion`
 - Show completion status
 - Not required

`--title`, `--description`, `--due-date`, `--weight`, `--folder`, `--last-updated`, `school-website`, and `--completion` are defaults unless at least one is specicied.

**Description** \
Echoes metadata on an assignment.