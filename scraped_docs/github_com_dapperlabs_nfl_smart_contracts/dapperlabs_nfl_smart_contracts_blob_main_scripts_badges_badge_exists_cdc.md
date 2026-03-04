# Source: https://github.com/dapperlabs/nfl-smart-contracts/blob/main/scripts/badges/badge_exists.cdc

```
import AllDay from "AllDay"

/// Checks if a badge with the specified slug exists
///
/// @param slug: The unique slug identifier of the badge to check
/// @return: True if the badge exists, false otherwise
access(all) fun main(slug: String): Bool {
    return AllDay.getBadge(slug) != nil
}

```