# Data Model

## Config
- Opening time: Time
- Deadlines: [Time]
- Target Participants/Capacity: Number

### Judging
- Application Questions: [String]
- Decision release: [Time]
- Acceptance critera (for example): AcceptanceConfig

### Roles
- Should be able to define the roles that are present, and what each role has
  read/write access to
- Defaults:
  - Administrator
  - Reviewer
  - Judge
  - Event helper
  - Attendee

### AcceptanceConfig
- Should contain criteria and a specification about how to aggregate them

## Users
- [auth: talk to Claude]
- Role: as defined in Config::Roles


