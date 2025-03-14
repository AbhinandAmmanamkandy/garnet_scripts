import git_utils

# Kernel SU
print("\n")
print("Getting Latest KernelSU...")
url = "https://github.com/tiann/KernelSU"
git_utils.get_latest_release(url)
print("KernelSU Download Finished!")

# Kernel SU Next
print("\n")
print("Getting Latest KernelSU Next...")
url = "https://github.com/KernelSU-Next/KernelSU-Next"
git_utils.get_latest_release(url)
print("KernelSU Download Finished!")

# Magisk
print("\n")
print("Getting Latest Magisk...")
url = "https://github.com/topjohnwu/Magisk"
git_utils.get_latest_release(url)
print("KernelSU Download Finished!")

# Safetynet
print("\n")
print("Getting Latest Safetynet...")
url = "https://github.com/chiteroman/PlayIntegrityFix"
git_utils.get_latest_release(url, True)
print("KernelSU Download Finished!")

# Zygisk Next
print("\n")
print("Getting Latest Zygisk Next...")
url = "https://github.com/Dr-TSNG/ZygiskNext"
git_utils.get_latest_release(url, True)
print("KernelSU Download Finished!")

# Zygisk Detach
print("\n")
print("Getting Latest Zygisk Detach...")
url = "https://github.com/j-hc/zygisk-detach"
git_utils.get_latest_release(url, True)
print("KernelSU Download Finished!")

# Google Photos
print("\n")
print("Getting Latest Revanced...")
url = "https://github.com/j-hc/revanced-magisk-module"
git_utils.get_latest_release(url, True)
print("KernelSU Download Finished!")

# Youtube Music
print("\n")
print("Getting Latest Revanced...")
url = "https://github.com/j-hc/revanced-magisk-module"
git_utils.get_latest_release(url, True)
print("KernelSU Download Finished!")

# Youtube
print("\n")
print("Getting Latest Revanced...")
url = "https://github.com/j-hc/revanced-magisk-module"
git_utils.get_latest_release(url, True)
print("KernelSU Download Finished!")

# LSPosed
print("\n")
print("Getting Latest LSPosed...")
url = "https://github.com/JingMatrix/LSPosed"
git_utils.get_latest_release(url, True)
print("LSPosed Download Finished!")

# AdAway
print("\n")
print("Downloading AdAway...")
url = "https://f-droid.org/repo/org.adaway_60104.apk"
git_utils.download_file(url, "AdAway.apk")
print("AdAway Download finished!")

# WaEnhancer
print("\n")
print("Downloading WaEnhancer...")
url = "https://github.com/Dev4Mod/WaEnhancer"
git_utils.get_latest_release(url)
print("AdAway Download finished!")