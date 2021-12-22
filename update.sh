if ! git diff-index --quiet HEAD --; then
    VN="$VN-mod"
	echo changed
fi