SmokeTest
=========

SmokeTest
-------------------
tags: smoke

Setup of contexts
* SmokeConfiguration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline-with-git-material" - setup
* With "1" live agents - setup
* Capture go state "SmokeTest" - setup

* Looking at pipeline "basic-pipeline-with-git-material"
* Trigger "basic-pipeline-with-git-material"
* Wait till pipeline completed
* Verify stage "defaultStage" is "Passed"

* On Preferences page
* Verify page title is "Preferences"

teardown
_______________
* Capture go state "SmokeTest" - teardown
* With "1" live agents - teardown
