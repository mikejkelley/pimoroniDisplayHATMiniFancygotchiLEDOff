# pimoroniDisplayHATMiniFancygotchiLEDOff
When run on Fancygotchi 2.0, the Pimoroni Display HAT Mini LED attempts to perform cheap, unauthorized eye surgery on its owner. This script prevents that and can be run at boot with the added .service file.

Copy turn_off_led.py to /home/pi/, typically via SFTP. Copy turn_off_led_on_boot.service to /etc/systemd/system/. Connect to your Fancygotchi via SSH and run the following command:
sudo systemctl daemon-reload

Enable the service to run at boot by running the following command:
sudo systemctl enable turn_off_led_at_boot.service

Then, reboot:
sudo reboot

That's it! You no longer have to fear that your pwnpet will burn out your eyes!
