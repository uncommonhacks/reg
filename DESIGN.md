# Uncommon Hacks Registration Platform

## Goal

This is a platform for hackathon registration. Applicants should be able to
submit their information, track their status, and be informed of their decision.
Administrators should be able to evaluate (admit, waitlist, deny) applicants
efficiently, configure [registration parameters](#registration-parameters)
(deadlines, etc.). It is somewhat based on
[Quill](https://github.com/techx/quill).

## Architecture Outline

### Registration Parameters

- Opening time: when the platform starts accepting applications.
- Deadlines: it should be possible to set one or more deadlines. These should be
  completely independent of individual status (for example, an applicant should
  be able to be waitlisted before the final deadline).
- Target Participants/Capacity: maybe only useful for displaying on admin pages.
- Application Questions: questions as well as their parameters (word limit,
  reviewing criteria).
- Decision release: admins should be allowed to manually release at any time
  (with warnings), list of dates should be configurable, can only release
  everything (i.e. cannot release any subset of decisions)
- Acceptance critera (for example):
  - Minimum number of reviewers
  - Reviewers can upvote, downvote, and maybe abstain/neutral vote?
  - Certain number of upvotes generates an acceptance (configurable)
  - Certain number of downvotes generates a rejection (configurable)
  - Neither generates a waitlist
  - TODO possibly add the ability to fine-grained acceptance criteria

### User Model

There are three types of users:

- Administrators
- Reviewing
- Event Helper
- Applicants

_Administrators_ have full access privileges. They can access all applicant
information (that is relevant to making admissions decisions). However, they do
not reviewer applicants or view decisions (only summary statistics) -- this is to
avoid bias. Additionally, they can modify registration parameters. All these
actions are logged.

_Reviewing_ don't have access to any PII, and are able to submit decisions on
applicants.

_Event helpers_ have access to day-of functionality. In particular, they can
check in applicants and view information such as dietary restrictions, etc. They
can see, but not modify registration parameters. They can only see information
relating to admitted applicants.

_Applicants_ can see only their own state and application, and general day-of
information. Applicants should be able to associate themselves with other
applicants (in order to form teams)

Should be able to register in teams. Don't hard-code whether people can be
accepted/rejected as a team

## Functionality

### Reviewing

- Administrators are able to specify, in some config interface, what our metrics
  for reviewing applicants are
- Reviewers should be able to submit decisions rating each candidate according to
  the administrators metrics and the ones on the questions. They should also be
  able to audit their own past reviews
- The system should have distinct steps for making a decision on a applicant and
  notifying applicants
    - This should be very obvious to users of the system -- reviewers should be
      aware of this
- Decisions should be immutable after they are released publically. The only
  allowable modification is removing people from the waitlist in either
  direction.
- There should be ways to general policies for reviewing
    - How many reviewers must review each applicant?
    - What's the minimum number of acceptances?
    - TODO some sort of data-driven way of accepting people, determined by
      config parameters
      - E.g. reviewers give upvotes, downvotes, neutral votes, a certain number of
        upvotes generates an acceptance, a certain number of downvotes generates
        a rejection, and neither generates a waitlist?

### Administration

- Administrators can specify configuration parameters for the event
  - Open and close date(s)
  - TODO add more
  - Surface summary statistics to show how changing config parameters impacts
    the whole admit pool.
- Administrators should be able to add new roles, and edit defaults through the
  interface
- Can release batches of decisions, but not see any PII (until after the
  application process closes, when they can export everything)
- Should be able to change roles, add new users, within PII boundaries
  - For example, someone who has had access to PII can't become an administrator
