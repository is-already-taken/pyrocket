#!/usr/bin/python

from rocket_backend import RocketManager
import time

class Base:

	def __init__(self):

		self.rocket_controller = RocketManager()
	
		err_msg = self.rocket_controller.acquire_devices()
		if err_msg:
			print "%s" % (err_msg)

	def get_active_launcher(self):
		if len(self.rocket_controller.launchers):
			return self.rocket_controller.launchers[0]

	def movement_wrapper(self, direction):
		launcher = self.get_active_launcher()

		if direction == 5:
			launcher.stop_movement()
			return False

		if direction == 4 or not (launcher.previous_limit_switch_states[direction] and not self.limit_override.get_active()):
			launcher.start_movement(direction)

			if direction == 4:
				return self.stop_charge.get_group()[self.CONTINUOUS_CHARGE].get_active()

			return True
		return False

	def move(self, direction):
		launcher = self.get_active_launcher()
		launcher.start_movement(direction)
		# self.movement_wrapper(direction)

	def stop(self):
		launcher = self.get_active_launcher()
		launcher.stop_movement()

	def main(self):
		self.move(2)
		time.sleep(1)
		self.stop()


if __name__ == "__main__":
	launcher = Base()
	launcher.main()

