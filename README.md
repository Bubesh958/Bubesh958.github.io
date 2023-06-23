```
make clean && make html && cd ../../ && mv ./notes/sphinx-doc/* .temp/ && rm -rd notes && mkdir notes && cd notes && mkdir sphinx-doc && cd sphinx-doc && mv ../../.temp/* . && cd ../ && mv ./sphinx-doc/build/html/* . && cd sphinx-doc
```
