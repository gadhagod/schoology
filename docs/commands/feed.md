### feed
Get your schoology feed.

**Syntax** \
`schoology feed [OPTIONS]`

**Options** 
- `--limit INTEGER`
 - Limit of results
 - Not required, defaults to ten
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
Echoes your schoology updates' metadata from all groups, section, and courses.