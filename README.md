# Trello Miner

Trello Miner extracts board, list and card data from the Trello API and writes this to a series of worksheets in an Excel workbook. As
a projects team at Internet Solutions, we wanted to use Trello for tracking projects and tasks within a team, but required methods of
reporting on project status to ops management and Exco level using a tool fit for their consumption.

## Installation

For the moment, clone the GitHub repo, fire up a virtualenv and:

`pip install .`

I'll eventually get this put together as a proper app on the Cheese Shop.

## Usage

Once installed, just run:

`$ trellominer`

It'll take some time to complete, but will eventually drop an Excel file in your home directory. This file will be named after the
`output_file_name` attribute in your config file, with the date specified in `YY-MM-DD` format at the end of the file name. Note,
you can override this by setting an environment variable called `TRELLO_OUTPUT_FILE`.

## Problems

Please open an issue on this repo and I'll dig in and get on it as soon as possible.

## Configuration

By default, Trello Miner will look for a config file in the root of your home directory. You can also set an environment variable
called `TRELLO_CONFIG` that points to a file called `trellominer.yaml`. The format of the file is as follows:

```yaml
api:
  url: "https://api.trello.com/1/"
  key: <your Trello API key>
  token: <your Trello API token
  organization: "<the name of your team/organization/crew"
  output_file_name: "<desired XLSX file name>"
```
You can get your Trello API authentication details from:

[https://trello.com/app-key]

## Copyright

Copyright &copy; 2017 Paul Stevens

## License

Licensed under the MIT License. See LICENSE for details.
