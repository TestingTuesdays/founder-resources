# Role and authorization matrix — copy to a private project

**Application, staging build and test date:**

| Role / tenant | Object / operation | Allowed? | API actual | UI actual | Evidence / defect |
| --- | --- | --- | --- | --- | --- |
| Anonymous | Private profile read | No | | | |
| Member A | Tenant B export | No | | | |
| Member A | Own record edit | As configured | | | |
| Removed collaborator | Previous share link | No | | | |

Test **both** permitted and denied operations at the server boundary. Use synthetic records and report any data cross-over as a release blocker. Record retest version, owner and result.
