from tafor.utils.check import CheckTaf, Listen
from tafor.utils.validator import Pattern, TafValidator, TafGrammar, TafParser, SigmetParser
from tafor.utils.aftn import AFTNMessage
from tafor.utils.modem import serialComm
from tafor.utils.pagination import paginate


def checkVersion(releaseVersion, currentVersion):
    def versionNum(version):
        version = version.replace('v', '')
        if 'beta' in version:
            version, betaNum = version.split('-beta')
        else:
            betaNum = None

        nums = version.split('.')
        stableNum = 0
        multiple = 100

        for n in nums:
            stableNum += int(n) * multiple
            multiple = multiple / 10

        return {
            'stable': stableNum,
            'beta':  betaNum
        }

    current = versionNum(currentVersion)
    release = versionNum(releaseVersion)
    hasNewVersion = False

    if release['stable'] > current['stable']:
        hasNewVersion = True

    if release['stable'] == current['stable']:
        if release['beta'] is None and current['beta']:
            hasNewVersion = True

        if release['beta'] and current['beta'] and release['beta'] > current['beta']:
            hasNewVersion = True

    return hasNewVersion

