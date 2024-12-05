Feature: Validate the car valuation feature

#  Background:
#    Given Launch the browser
#    When Open the cashforyourwheels website
#
#
  @test
  Scenario: validate car valuation using input files
    Given User launch the browser and Open the URL
    #When User searches the details of the cars whose registration numbers present in the input file
    Then User should see the displayed car details matches the expected details from the output file