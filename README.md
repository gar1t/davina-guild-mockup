# Inputer/Predicter Mockup

## Setup

To isolate runs related to this work, it's a good idea to create an
environment.

    $ guild init

Review the settings and press `Enter` to create the environment.

NOTE: Guild environments are standard Python virtual environments. You
can alternatively create an environment using `virtualenv`, the `venv`
module, or `conda` according to your preference.

Activate the environment:

    $ source guild-env

If you create an environment using a different method, activate the
environment using the steps for that method.

## Project Help

To get help for the project, run:

    $ guild help

This information is generated from [guild.yml](guild.yml) and imported
flags from the applicable modules.

## Generate all Imputers

To generate all imputers (according to `imputer-all` - see
[guild.yml](guild.yml) for details), run:

    $ guild run all-imputers

Press `Enter` to start the operation.

Guild runs `imputer` for each of the specified flag combinations
defined in `all-imputers`.

Review the generated runs:

    $ guild runs

## TODO

- Hook up predictive models

Given that this is intended as a single pipeline, it's likely we
extend this single operation to support predictor model types and
hyperparameters and run all possible scenarios running a large grid
search. Each run would produce metrics associated with the imputer and
predictor.

If the imputers and predictors need to be separated, we need to figure
out how to drive predictors per generated imputers. Guild can handle
this easily enough with a single imputer but not with a set of
generated imputers. This would be an interesting feature enhancement
for Guild though!
