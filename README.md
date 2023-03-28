# ECC

Task is about:
It is checked whether all extra margins (i.e. margins calculated by ECC and uploaded to Prisma via upload file) shown in CC050 (Risk Engine report) of the previous business day are included in the first CI050 (Prisma report) of the day as well as the last CI050 of the previous day and vice versa.
This has to be done for a configurable list of margin classes, at the moment:

SPAN
IMSM
CESM
AMPO
AMEM
AMCO
AMCU
AMWI
DMEM


The check is executed when both CC050 and first CI050 are received.
In case of error detection, an email is sent to a configurable list of recipients, stating the report and details of the found exception.
Also the error is logged so a PMA could be used for monitoring.
