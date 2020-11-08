### updates
Get updates of a section or group

**Syntax** \
`schoology updates [OPTIONS]`

**Options** 
- `--limit INTEGER`
 - Limit of results
 - Not required, defaults to ten
- `--section TEXT`
 - Show updates of a section
 - Required if `--group` is not specified
- `--group TEXT`
 - Show updates of a group
 - Required if `--section` is not specified
- `--id`
 - Show ID
 - Not required
- `--likes`
 - Show like count
 - Not required
- `--comments`
 - Show comment count
 - Not required
- `--time`
 - Show time when posted
 - Not required
- `--body`
 - Show body
 - Not required

`--id`, `--likes`, `--comments`, `--time`, and `--body` are defaults unless at least one is specicied.

**Description** \
Echoes schoology updates and metadata from a group or sections.