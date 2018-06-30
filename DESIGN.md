# Uncommon Hacks Registration Platform

## Goal

This is a platform for hackathon registration. Applicants should be able to submit their information, track their status, and be informed of their decision. Administrators should be able to evaluate (admit, waitlist, deny) applicants efficiently, configure [registration parameters](#registration-parameters) (deadlines, etc.). It is somewhat based on [Quill](https://github.com/techx/quill).

## Functionality

TODO

### Registration Parameters

- Opening time: when the platform starts accepting applications.
- Deadlines: it should be possible to set one or more deadlines. These should be completely independent of individual status (for example, an applicant should be able to be waitlisted before the final deadline).
- Target Participants/Capacity: maybe only useful for displaying on admin pages.
- Application Questions: questions as well as their parameters (word limit, judging criteria).

### User Model

There are three types of users:

- Administrators
- Event Helper
- Applicants

_Administrators_ have full access privileges. They can access all applicant information (that is relevant to making admissions decisions), judge applicants, and submit final decisions. Additionally, they can modify registration parameters. All these actions are logged.

_Event helpers_ have access to day-of functionality. In particular, they can check in applicants and view information such as dietary restrictions, etc. They can see, but not modify registration parameters. They can only see information relating to admitted applicants.
