install: installLocal

remove: removeLocal removeGlobal

installLocal:
	mkdir -p $(HOME)/.scripts/screenlayout-chooser
	cp -r ./ $(HOME)/.scripts/screenlayout-chooser
	chown $(USER):users -R $(HOME)/.scripts/screenlayout-chooser

removeLocal:
	rm -rf $(HOME)/.scripts/screenlayout-chooser

installGlobal:
	mkdir -p /opt/scripts/screenlayout-chooser
	cp -r ./ /opt/scripts/screenlayout-chooser
	chown root:root -R /opt/scripts/screenlayout-chooser

removeGlobal:
	rm -rf /opt/scripts/screenlayout-chooser
