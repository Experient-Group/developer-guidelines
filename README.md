# 👩🏻‍💻 🧑‍💻 Experient Group
##  Developer Guidelines

Experient Group is a business + IT consultancy that strives to serve our clients and our people better than anyone else.
This document serves to exist as a reference for developers. Please update the information in this document to keep it up-to-date.

## Tooling

Developer tools (or "development tools" or short "DevTools") are programs that allow a developer to create, test and debug software. 

- https://www.sourcetreeapp.com/

- https://iterm2.com/

- https://ohmyz.sh/

- https://code.visualstudio.com/download

- https://www.jetbrains.com/idea/download/


## Git
Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development.

1) Create an account at [GitHub](https://github.com/)

2) Adding & Updating GitHub Access Token on Mac

    Follow the instructions on Github to [Create an Access Token in Github](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
    
    ### Configure Git to use the osxkeychain
    
    By default, git credentials are not cached so you need to tell Git if you want to avoid having to provide them each time Github requires you to authenticate. On Mac, Git comes with an “osxkeychain” mode, which caches credentials in the secure keychain that’s attached to your system account.
    
    You can tell Git you want to store credentials in the osxkeychain by running the following:-
    
    ```sh
    git config --global credential.helper osxkeychain
    ```
    
    ### Add your access token to the osxkeychain
    
    Now issue a command to interract with Github which requires authentication, eg. `git clone` or `git pull`. When you are prompted to supply your _Password for 'https://username@github.com':_ you enter your access token instead. Your token should now get cached in the osxkeychain automatically.
    
    ```sh
    $ git clone https://github.com/username/repo.git
    
    Cloning into 'repo'...
    Username for 'https://github.com': your_github_username
    Password for 'https://username@github.com': your_access_token
    ```


For more information please reference this link:
https://gist.github.com/jonjack/bf295d4170edeb00e96fb158f9b1ba3c


## Git Best Practices
#### Standards for Repositories
- __Never upload private code__
Cloning repos are necessary for work, but there is __NEVER__ a reason you should upload code you have written for a client publically. There are plenty of open source contributions you can make. Code created on behalf Experient Group is not the property of the indiviudal.
__DO NOT UPLOAD ANY PRIVATE REPOS__

- __No Secrets__ 
No secrets, including passwords and API keys, can be included in source control.

- __Documented with Read Me__
There must be a readme.md file with context about the project in its root directory. At a bare minimum, this should include a link to other documentation if it exists (e.g., in Confluence), how to build/install, and a link to the pipeline (see below).

- __Sign commit messages__

#### Branch Naming Standards
Any feature or bugfix work will be done on its own branch. Feature branches are to be prefixed with f/ and bugfix branches are to be prefixed with b/. Continue to follow this pattern in the event of other types of work; for example, if something like an integration branch is needed prefix the branch with i/, and so on. Each branch name should also be appended with the Jira ticket the work corresponds to, which allows for automatic integration with that tool. 

Examples:
`b/daypart-handling_DLP5-34`
`f/timer-highlight_DLP5-78`


#### How to Write Commit Message
Commit messages matter. Here's how to write them well.

Examples:
https://cbea.ms/git-commit/

## Code Reviews

Any time a new feature or fix is being worked on, the engineer should:

1) Create a new branch locally to make the necessary changes. This should always be branched from the remote develop branch.


2) Commit Message Standards - All commits should follow these standards:


3) Commit starts with a short header explaining change

    - Separate subject from body with a blank line
    - Limit the subject line to ~50 characters
    - Include descriptive body, preferrably bullet pointed
    - Use the body to explain what and why vs. how

4) When the changes are ready for review, push the branch up to the remote repo.

5) Try to keep a PR under 400 lines so its scope will be reasonable for the reviewer, if possible to break up a large change into multiple smaller PRs, do so.

6) Don’t mix large code-cleanup work with feature development - put it in it’s own PR so the actual code change will be obvious to the reviewer.

7) Open a PR for merging the branch to develop. The PR title should have a descriptive name that indicates the feature or fix being addressed.

8) Use the PR description field and/or a combination of inline code-notes or PR comments to explain anything not already obvious from the individual commit messages.  This will especially apply to architectural or wide-spanning changes.

9) Once the PR is created, GitHub will automatically assign two reviewers based on a rotation of the team.  Let’s try this for a while as it would be good for cross-training.  This is part of why the above documentation steps are so important.  If a particular PR is critical to work another team member is performing, you can manually select that person. GitHub will then auto-assign just one additional team member for review.

10) Review the PR checks to make sure everything is green rather than waiting to let the reviewer discover this.  Fix any issue immediately while this code change is fresh in your mind, and so the Reviewer doesn’t get held up by this or see your failing checks and delay the review unnecessarilly.

#### Conducting Code Reviews
When conducting a review, please bear in mind the above goals of the code review. Specifically, when reviewing code, there are some best practices to keep in mind:

- Look for clarity. You should generally be able to understand what the code is doing by reading it. While you may occasionally need to reach out to the developer to clarify certain things (especially if dealing with a brand-new framework or project), this should not be regular practice and is probably an indication the code is not clear enough.  

- Short methods are preferred for readability - if a comment is required to explain part of a function, it is a good indicator that the function should be split up and the function names used for clarity.

- Check for classes growing too large - does this code belong in this class or would it be more clear broken out into another class?

- Variable names must be self-explanatory - if a choice must be made, prefer longer understandable names over short cryptic ones.

- Look for simplicity.  Is it possible to solve this problem in a simpler way?  Does the solution adhere to Separation of Concerns and SRS (Single Responsibility Principle)?

- Look for defects. While not the only goal of code reviews, they are intended to help catch non-functioning, insecure, or error-prone code.

- Check for adequate testing.  If code changed, tests should change too.  If new functionality was added, there should be a series of new tests covering both the normal code flow but also the edge/error cases.  Check, but don’t rely on the code coverage number, because code coverage only indicates a line of code was run by a test, not that it’s behavior was actually verified by the test.

- Don’t nitpick on style. While style is important, it is a secondary concern in code reviews (this should largely be handled by a linting step anyway). You may still point out significant style/syntax issues that you find, but it should not be your primary focus during review (especially as we don’t have an established style guide we’re following).

- Call out positives too. There’s a tendency to focus on finding defects and things to fix in code reviews, but they are also an opportunity to let someone know when they did well. If you see a particularly clever or insightful piece of code, let them know!

- Don’t require perfection before approving.  Make sure the important things here are taken care of before approving the PR, but for more minor things go ahead and approve so the implementer can fix and merge without another checkpoint.


#### Timing of Code Reviews
Each team member should allot some time each day for reviewing code in their PR queue. Some guidelines to bear in mind regarding time spent on reviews:

- For simpler PRs, try to review them as they are received. More complicated/longer PRs may be set aside for another time in the day.

- Make an effort to empty your PR queue each day, as open PRs represent blockers for other pod members. 

- Code reviews should not take up more than an hour of your day. While time spent each day on code reviews will vary, 15-30 minutes should be more the norm. If you find yourself consistently spending way more time on them, reach out to the engineering lead as it may mean we need to re-consider how PR reviews are being assigned.

## Design Patterns

A software design pattern is a general, reusable solution to a commonly occurring problem within a given context in software design.

>The Gang of Four (Gof) Patterns are a group of twenty three Design Patterns originally published in a seminal book entitled Design Patterns: Elements of Reusable Object-Oriented Software; the term 'Gang of Four' refers to the four authors.

The GoF Design Patterns are broken into three categories: Creational Patterns for the creation of objects; Structural Patterns to provide relationship between objects; and finally, Behavioral Patterns to help define how objects interact.

### Creational
 ###### [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

#### Structural
 ###### [Adapter](https://refactoring.guru/design-patterns/adapter)
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.


#### Behavioral
 ###### [Observer](https://refactoring.guru/design-patterns/observer)
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
 
### Additional Design Pattern Resources:

#### [Refactoring Guru](https://refactoring.guru/design-patterns/python)
#### [Geeks for Geeks](https://www.geeksforgeeks.org/python-design-patterns/)
#### [Journal Dev](https://www.journaldev.com/31902/gangs-of-four-gof-design-patterns)


## Next Steps


