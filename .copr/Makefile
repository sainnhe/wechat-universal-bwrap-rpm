srpm:
	./download-deb.sh
	rpmbuild -bs --define "_sourcedir src" --define "_srcrpmdir $(outdir)" $(spec)
