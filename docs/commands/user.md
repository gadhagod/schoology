### user
Get data on a user.

**Syntax** \
`schoology user [OPTIONS] USER_ID`

**Options** 
- `--limit INTEGER`
 - Limit of results
 - Not required, defaults to ten
- `--name`
 - Show name
 - Not required
- `--email`
 - Show email
 - Not required
- `--school-id`
 - Show school id
 - Not required
- `--school-name`
 - Show school name
 - Not required
- `--school-location`
 - Show school location
 - Not required
- `--school-postal-code`
 - Show school postal code
 - Not required
- `school-website`
 - Show school website
 - Not required
- `school-phone`
 - Show school phone number
 - Not required

`--name`, `--email`, `--school-id`, `--school-name`, `--school-location`, `--school-postal-code`, `school-website`, and `--school-phone` are defaults unless at least one is specicied.

**Description** \
Echoes metadata on a user.