# Health-Study-Python
Python analysis project of health data.

## Arbetsmoment
- numpy, pandas, matplotlib.
- scipy, scikit-learn, statsmodels.
- multiple linear regression, error analysis.
- Principal Component Analysis, egenvektorer.
- dataclass, class (OOP).
- simulation: bootstrap, Welch t-test, confidence interval, power.
- git bash, python- & mathematical documentation.

## Resultat
**Blodtryck** modellerad som funktion av ålder och vikt:
| Intercept | Coeff 1: Ålder | Coeff 2: Vikt | R^2 |
| --------- | -------------- | ------------- | --- |
| 109.50    | 0.54 | 0.18 | 0.405 |

**Konfidensintervall**:
| Metod | Intervall |
| ----- | ------ |
| Normalapproximation | 148.29, 150.06 |
| Bootstrap | 148.31, 150.10 |

**Hypotesprövning**:
Skillnad i medelblodtryck: 0.47 mmHg
| Bootstrap CI | -1.48, 2.48 |
| Welch t-test | t = 0.45, p = 0.653 |
Då intervallet innehåller 0, och *p* > 0.05 förkastas inte nollhypotesen.

### PCA
![PCA](https://github.com/MaWe96/Health-Study-Python/blob/main/Results/PCA.png)

**PCA** visade mer strukturen i data än separation av klasser.

### Power
![Power](https://github.com/MaWe96/Health-Study-Python/blob/main/Results/Power.png)

Det krävs stora stickprov för att upptäcka skillnad.

## References:
- Wackerly, D., Mendenhall, W., Scheaffer, R. (2014). Mathematical Statistics with Applications, 7th Edition, Cengage Learning.
- Anton, H., Rorres, C. (2014). Elementary Linear Algebra: Applications Version, 11th Edition, Wiley.
- Mathews, J., Fink, K. (2004). *Numerical Methods using MATLAB*, 4th Edition, Pearson.

Python version: 3.14.0
