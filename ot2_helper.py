from opentrons import protocol_api
import time, json

class OT2Helper():

    protocol = None

    def __init__(self, protocol):
        
        self.protocol = protocol

    def blink_one(self):

        time.sleep(1)

        self.protocol.set_rail_lights(True)

        time.sleep(1)

        self.protocol.set_rail_lights(False)

        time.sleep(1)

        self.protocol.set_rail_lights(True)

        time.sleep(1)

    def blink_three(self):

        time.sleep(1)

        self.protocol.set_rail_lights(True)

        for i in range(1,4):

            time.sleep(1)

            self.protocol.set_rail_lights(False)

            time.sleep(1)

            self.protocol.set_rail_lights(True)

        time.sleep(1)

    def move_aspirate(self, volume, k, source, dest, pipette):

        pipette.move_to(source.top(z=-17))

        pipette.aspirate(50)

        pipette.move_to(source.top(z=-30))

        pipette.aspirate(200)

        pipette.move_to(source.top(z=-43))

        pipette.aspirate(50)

        pipette.dispense(300, dest.top())

        

        # for i in range(1, 44):

        #     pipette.move_to(source.top(z=-i))

        #     pipette.aspirate()




metadata = {'apiLevel': '2.6'}


def run(protocol: protocol_api.ProtocolContext):
    with open('/data/labware/v2/custom_definitions/micronic_96_tuberack_1400ul.json') as labware_file:
        labware_def = json.load(labware_file)

    micronic = protocol.load_labware_from_definition(labware_def, 1)
    tiprack_1 = protocol.load_labware("opentrons_96_tiprack_300ul", 5)
    pipette = protocol.load_instrument('p300_single_gen2', mount='left')
    mag_mod = protocol.load_module('magnetic module gen2', '7')

    pipette.pick_up_tip(tiprack_1["H12"])

    helper = OT2Helper(protocol)

    helper.blink_one()

    helper.move_aspirate(10, 0, micronic["H12"], micronic["H11"], pipette)

    helper.blink_one()

    pipette.drop_tip(tiprack_1["H12"])




    