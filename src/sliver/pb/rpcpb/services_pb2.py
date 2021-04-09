# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpcpb/services.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..commonpb import common_pb2 as commonpb_dot_common__pb2
from ..sliverpb import sliver_pb2 as sliverpb_dot_sliver__pb2
from ..clientpb import client_pb2 as clientpb_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpcpb/services.proto',
  package='rpcpb',
  syntax='proto3',
  serialized_options=b'Z*github.com/bishopfox/sliver/protobuf/rpcpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14rpcpb/services.proto\x12\x05rpcpb\x1a\x15\x63ommonpb/common.proto\x1a\x15sliverpb/sliver.proto\x1a\x15\x63lientpb/client.proto2\xe1\"\n\tSliverRPC\x12\x30\n\nGetVersion\x12\x0f.commonpb.Empty\x1a\x11.clientpb.Version\x12\x34\n\x0cGetOperators\x12\x0f.commonpb.Empty\x1a\x13.clientpb.Operators\x12\x32\n\x0bGetSessions\x12\x0f.commonpb.Empty\x1a\x12.clientpb.Sessions\x12\x38\n\x0bKillSession\x12\x18.sliverpb.KillSessionReq\x1a\x0f.commonpb.Empty\x12;\n\rUpdateSession\x12\x17.clientpb.UpdateSession\x1a\x11.clientpb.Session\x12*\n\x07GetJobs\x12\x0f.commonpb.Empty\x1a\x0e.clientpb.Jobs\x12\x32\n\x07KillJob\x12\x14.clientpb.KillJobReq\x1a\x11.clientpb.KillJob\x12\x46\n\x11StartMTLSListener\x12\x19.clientpb.MTLSListenerReq\x1a\x16.clientpb.MTLSListener\x12@\n\x0fStartWGListener\x12\x17.clientpb.WGListenerReq\x1a\x14.clientpb.WGListener\x12\x43\n\x10StartDNSListener\x12\x18.clientpb.DNSListenerReq\x1a\x15.clientpb.DNSListener\x12G\n\x12StartHTTPSListener\x12\x19.clientpb.HTTPListenerReq\x1a\x16.clientpb.HTTPListener\x12\x46\n\x11StartHTTPListener\x12\x19.clientpb.HTTPListenerReq\x1a\x16.clientpb.HTTPListener\x12O\n\x16StartTCPStagerListener\x12\x1b.clientpb.StagerListenerReq\x1a\x18.clientpb.StagerListener\x12P\n\x17StartHTTPStagerListener\x12\x1b.clientpb.StagerListenerReq\x1a\x18.clientpb.StagerListener\x12\x35\n\x08Generate\x12\x15.clientpb.GenerateReq\x1a\x12.clientpb.Generate\x12\x39\n\nRegenerate\x12\x17.clientpb.RegenerateReq\x1a\x12.clientpb.Generate\x12\x39\n\rImplantBuilds\x12\x0f.commonpb.Empty\x1a\x17.clientpb.ImplantBuilds\x12:\n\x12\x44\x65leteImplantBuild\x12\x13.clientpb.DeleteReq\x1a\x0f.commonpb.Empty\x12/\n\x08\x43\x61naries\x12\x0f.commonpb.Empty\x1a\x12.clientpb.Canaries\x12\x43\n\x16GenerateWGClientConfig\x12\x0f.commonpb.Empty\x1a\x18.clientpb.WGClientConfig\x12\x39\n\x10GenerateUniqueIP\x12\x0f.commonpb.Empty\x1a\x14.clientpb.UniqueWGIP\x12=\n\x0fImplantProfiles\x12\x0f.commonpb.Empty\x1a\x19.clientpb.ImplantProfiles\x12<\n\x14\x44\x65leteImplantProfile\x12\x13.clientpb.DeleteReq\x1a\x0f.commonpb.Empty\x12H\n\x12SaveImplantProfile\x12\x18.clientpb.ImplantProfile\x1a\x18.clientpb.ImplantProfile\x12\x37\n\x08MsfStage\x12\x16.clientpb.MsfStagerReq\x1a\x13.clientpb.MsfStager\x12\x41\n\x0cShellcodeRDI\x12\x19.clientpb.ShellcodeRDIReq\x1a\x16.clientpb.ShellcodeRDI\x12/\n\x08Websites\x12\x0f.commonpb.Empty\x1a\x12.clientpb.Websites\x12/\n\x07Website\x12\x11.clientpb.Website\x1a\x11.clientpb.Website\x12\x33\n\rWebsiteRemove\x12\x11.clientpb.Website\x1a\x0f.commonpb.Empty\x12\x43\n\x11WebsiteAddContent\x12\x1b.clientpb.WebsiteAddContent\x1a\x11.clientpb.Website\x12\x46\n\x14WebsiteUpdateContent\x12\x1b.clientpb.WebsiteAddContent\x1a\x11.clientpb.Website\x12I\n\x14WebsiteRemoveContent\x12\x1e.clientpb.WebsiteRemoveContent\x1a\x11.clientpb.Website\x12&\n\x04Ping\x12\x0e.sliverpb.Ping\x1a\x0e.sliverpb.Ping\x12#\n\x02Ps\x12\x0f.sliverpb.PsReq\x1a\x0c.sliverpb.Ps\x12\x38\n\tTerminate\x12\x16.sliverpb.TerminateReq\x1a\x13.sliverpb.Terminate\x12\x35\n\x08Ifconfig\x12\x15.sliverpb.IfconfigReq\x1a\x12.sliverpb.Ifconfig\x12\x32\n\x07Netstat\x12\x14.sliverpb.NetstatReq\x1a\x11.sliverpb.Netstat\x12#\n\x02Ls\x12\x0f.sliverpb.LsReq\x1a\x0c.sliverpb.Ls\x12$\n\x02\x43\x64\x12\x0f.sliverpb.CdReq\x1a\r.sliverpb.Pwd\x12&\n\x03Pwd\x12\x10.sliverpb.PwdReq\x1a\r.sliverpb.Pwd\x12#\n\x02Rm\x12\x0f.sliverpb.RmReq\x1a\x0c.sliverpb.Rm\x12,\n\x05Mkdir\x12\x12.sliverpb.MkdirReq\x1a\x0f.sliverpb.Mkdir\x12\x35\n\x08\x44ownload\x12\x15.sliverpb.DownloadReq\x1a\x12.sliverpb.Download\x12/\n\x06Upload\x12\x13.sliverpb.UploadReq\x1a\x10.sliverpb.Upload\x12>\n\x0bProcessDump\x12\x18.sliverpb.ProcessDumpReq\x1a\x15.sliverpb.ProcessDump\x12,\n\x05RunAs\x12\x12.sliverpb.RunAsReq\x1a\x0f.sliverpb.RunAs\x12>\n\x0bImpersonate\x12\x18.sliverpb.ImpersonateReq\x1a\x15.sliverpb.Impersonate\x12\x38\n\tRevToSelf\x12\x16.sliverpb.RevToSelfReq\x1a\x13.sliverpb.RevToSelf\x12\x38\n\tGetSystem\x12\x16.clientpb.GetSystemReq\x1a\x13.sliverpb.GetSystem\x12)\n\x04Task\x12\x11.sliverpb.TaskReq\x1a\x0e.sliverpb.Task\x12(\n\x03Msf\x12\x10.clientpb.MSFReq\x1a\x0f.commonpb.Empty\x12\x34\n\tMsfRemote\x12\x16.clientpb.MSFRemoteReq\x1a\x0f.commonpb.Empty\x12J\n\x0f\x45xecuteAssembly\x12\x1c.sliverpb.ExecuteAssemblyReq\x1a\x19.sliverpb.ExecuteAssembly\x12\x32\n\x07Migrate\x12\x14.clientpb.MigrateReq\x1a\x11.sliverpb.Migrate\x12\x32\n\x07\x45xecute\x12\x14.sliverpb.ExecuteReq\x1a\x11.sliverpb.Execute\x12<\n\x0c\x45xecuteToken\x12\x19.sliverpb.ExecuteTokenReq\x1a\x11.sliverpb.Execute\x12\x35\n\x08Sideload\x12\x15.sliverpb.SideloadReq\x1a\x12.sliverpb.Sideload\x12;\n\x08SpawnDll\x12\x1b.sliverpb.InvokeSpawnDllReq\x1a\x12.sliverpb.SpawnDll\x12;\n\nScreenshot\x12\x17.sliverpb.ScreenshotReq\x1a\x14.sliverpb.Screenshot\x12;\n\nNamedPipes\x12\x17.sliverpb.NamedPipesReq\x1a\x14.sliverpb.NamedPipes\x12\x38\n\x0bTCPListener\x12\x15.sliverpb.TCPPivotReq\x1a\x12.sliverpb.TCPPivot\x12\x39\n\nListPivots\x12\x16.sliverpb.PivotListReq\x1a\x13.sliverpb.PivotList\x12@\n\x0cStartService\x12\x19.sliverpb.StartServiceReq\x1a\x15.sliverpb.ServiceInfo\x12>\n\x0bStopService\x12\x18.sliverpb.StopServiceReq\x1a\x15.sliverpb.ServiceInfo\x12\x42\n\rRemoveService\x12\x1a.sliverpb.RemoveServiceReq\x1a\x15.sliverpb.ServiceInfo\x12\x38\n\tMakeToken\x12\x16.sliverpb.MakeTokenReq\x1a\x13.sliverpb.MakeToken\x12-\n\x06GetEnv\x12\x10.sliverpb.EnvReq\x1a\x11.sliverpb.EnvInfo\x12/\n\x06SetEnv\x12\x13.sliverpb.SetEnvReq\x1a\x10.sliverpb.SetEnv\x12\x35\n\x08\x42\x61\x63kdoor\x12\x15.sliverpb.BackdoorReq\x1a\x12.sliverpb.Backdoor\x12\x41\n\x0cRegistryRead\x12\x19.sliverpb.RegistryReadReq\x1a\x16.sliverpb.RegistryRead\x12\x44\n\rRegistryWrite\x12\x1a.sliverpb.RegistryWriteReq\x1a\x17.sliverpb.RegistryWrite\x12P\n\x11RegistryCreateKey\x12\x1e.sliverpb.RegistryCreateKeyReq\x1a\x1b.sliverpb.RegistryCreateKey\x12,\n\x05Shell\x12\x12.sliverpb.ShellReq\x1a\x0f.sliverpb.Shell\x12\x32\n\x0c\x43reateTunnel\x12\x10.sliverpb.Tunnel\x1a\x10.sliverpb.Tunnel\x12\x30\n\x0b\x43loseTunnel\x12\x10.sliverpb.Tunnel\x1a\x0f.commonpb.Empty\x12<\n\nTunnelData\x12\x14.sliverpb.TunnelData\x1a\x14.sliverpb.TunnelData(\x01\x30\x01\x12,\n\x06\x45vents\x12\x0f.commonpb.Empty\x1a\x0f.clientpb.Event0\x01\x42,Z*github.com/bishopfox/sliver/protobuf/rpcpbb\x06proto3'
  ,
  dependencies=[commonpb_dot_common__pb2.DESCRIPTOR,sliverpb_dot_sliver__pb2.DESCRIPTOR,clientpb_dot_client__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_SLIVERRPC = _descriptor.ServiceDescriptor(
  name='SliverRPC',
  full_name='rpcpb.SliverRPC',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=101,
  serialized_end=4550,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetVersion',
    full_name='rpcpb.SliverRPC.GetVersion',
    index=0,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._VERSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOperators',
    full_name='rpcpb.SliverRPC.GetOperators',
    index=1,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._OPERATORS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSessions',
    full_name='rpcpb.SliverRPC.GetSessions',
    index=2,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._SESSIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='KillSession',
    full_name='rpcpb.SliverRPC.KillSession',
    index=3,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._KILLSESSIONREQ,
    output_type=commonpb_dot_common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateSession',
    full_name='rpcpb.SliverRPC.UpdateSession',
    index=4,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._UPDATESESSION,
    output_type=clientpb_dot_client__pb2._SESSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetJobs',
    full_name='rpcpb.SliverRPC.GetJobs',
    index=5,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._JOBS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='KillJob',
    full_name='rpcpb.SliverRPC.KillJob',
    index=6,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._KILLJOBREQ,
    output_type=clientpb_dot_client__pb2._KILLJOB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartMTLSListener',
    full_name='rpcpb.SliverRPC.StartMTLSListener',
    index=7,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._MTLSLISTENERREQ,
    output_type=clientpb_dot_client__pb2._MTLSLISTENER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartWGListener',
    full_name='rpcpb.SliverRPC.StartWGListener',
    index=8,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._WGLISTENERREQ,
    output_type=clientpb_dot_client__pb2._WGLISTENER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartDNSListener',
    full_name='rpcpb.SliverRPC.StartDNSListener',
    index=9,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._DNSLISTENERREQ,
    output_type=clientpb_dot_client__pb2._DNSLISTENER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartHTTPSListener',
    full_name='rpcpb.SliverRPC.StartHTTPSListener',
    index=10,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._HTTPLISTENERREQ,
    output_type=clientpb_dot_client__pb2._HTTPLISTENER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartHTTPListener',
    full_name='rpcpb.SliverRPC.StartHTTPListener',
    index=11,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._HTTPLISTENERREQ,
    output_type=clientpb_dot_client__pb2._HTTPLISTENER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartTCPStagerListener',
    full_name='rpcpb.SliverRPC.StartTCPStagerListener',
    index=12,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._STAGERLISTENERREQ,
    output_type=clientpb_dot_client__pb2._STAGERLISTENER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartHTTPStagerListener',
    full_name='rpcpb.SliverRPC.StartHTTPStagerListener',
    index=13,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._STAGERLISTENERREQ,
    output_type=clientpb_dot_client__pb2._STAGERLISTENER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Generate',
    full_name='rpcpb.SliverRPC.Generate',
    index=14,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._GENERATEREQ,
    output_type=clientpb_dot_client__pb2._GENERATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Regenerate',
    full_name='rpcpb.SliverRPC.Regenerate',
    index=15,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._REGENERATEREQ,
    output_type=clientpb_dot_client__pb2._GENERATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ImplantBuilds',
    full_name='rpcpb.SliverRPC.ImplantBuilds',
    index=16,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._IMPLANTBUILDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteImplantBuild',
    full_name='rpcpb.SliverRPC.DeleteImplantBuild',
    index=17,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._DELETEREQ,
    output_type=commonpb_dot_common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Canaries',
    full_name='rpcpb.SliverRPC.Canaries',
    index=18,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._CANARIES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateWGClientConfig',
    full_name='rpcpb.SliverRPC.GenerateWGClientConfig',
    index=19,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._WGCLIENTCONFIG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateUniqueIP',
    full_name='rpcpb.SliverRPC.GenerateUniqueIP',
    index=20,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._UNIQUEWGIP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ImplantProfiles',
    full_name='rpcpb.SliverRPC.ImplantProfiles',
    index=21,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._IMPLANTPROFILES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteImplantProfile',
    full_name='rpcpb.SliverRPC.DeleteImplantProfile',
    index=22,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._DELETEREQ,
    output_type=commonpb_dot_common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SaveImplantProfile',
    full_name='rpcpb.SliverRPC.SaveImplantProfile',
    index=23,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._IMPLANTPROFILE,
    output_type=clientpb_dot_client__pb2._IMPLANTPROFILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MsfStage',
    full_name='rpcpb.SliverRPC.MsfStage',
    index=24,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._MSFSTAGERREQ,
    output_type=clientpb_dot_client__pb2._MSFSTAGER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ShellcodeRDI',
    full_name='rpcpb.SliverRPC.ShellcodeRDI',
    index=25,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._SHELLCODERDIREQ,
    output_type=clientpb_dot_client__pb2._SHELLCODERDI,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Websites',
    full_name='rpcpb.SliverRPC.Websites',
    index=26,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._WEBSITES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Website',
    full_name='rpcpb.SliverRPC.Website',
    index=27,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._WEBSITE,
    output_type=clientpb_dot_client__pb2._WEBSITE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WebsiteRemove',
    full_name='rpcpb.SliverRPC.WebsiteRemove',
    index=28,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._WEBSITE,
    output_type=commonpb_dot_common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WebsiteAddContent',
    full_name='rpcpb.SliverRPC.WebsiteAddContent',
    index=29,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._WEBSITEADDCONTENT,
    output_type=clientpb_dot_client__pb2._WEBSITE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WebsiteUpdateContent',
    full_name='rpcpb.SliverRPC.WebsiteUpdateContent',
    index=30,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._WEBSITEADDCONTENT,
    output_type=clientpb_dot_client__pb2._WEBSITE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WebsiteRemoveContent',
    full_name='rpcpb.SliverRPC.WebsiteRemoveContent',
    index=31,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._WEBSITEREMOVECONTENT,
    output_type=clientpb_dot_client__pb2._WEBSITE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='rpcpb.SliverRPC.Ping',
    index=32,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._PING,
    output_type=sliverpb_dot_sliver__pb2._PING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ps',
    full_name='rpcpb.SliverRPC.Ps',
    index=33,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._PSREQ,
    output_type=sliverpb_dot_sliver__pb2._PS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Terminate',
    full_name='rpcpb.SliverRPC.Terminate',
    index=34,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._TERMINATEREQ,
    output_type=sliverpb_dot_sliver__pb2._TERMINATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ifconfig',
    full_name='rpcpb.SliverRPC.Ifconfig',
    index=35,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._IFCONFIGREQ,
    output_type=sliverpb_dot_sliver__pb2._IFCONFIG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Netstat',
    full_name='rpcpb.SliverRPC.Netstat',
    index=36,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._NETSTATREQ,
    output_type=sliverpb_dot_sliver__pb2._NETSTAT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ls',
    full_name='rpcpb.SliverRPC.Ls',
    index=37,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._LSREQ,
    output_type=sliverpb_dot_sliver__pb2._LS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Cd',
    full_name='rpcpb.SliverRPC.Cd',
    index=38,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._CDREQ,
    output_type=sliverpb_dot_sliver__pb2._PWD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Pwd',
    full_name='rpcpb.SliverRPC.Pwd',
    index=39,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._PWDREQ,
    output_type=sliverpb_dot_sliver__pb2._PWD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Rm',
    full_name='rpcpb.SliverRPC.Rm',
    index=40,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._RMREQ,
    output_type=sliverpb_dot_sliver__pb2._RM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Mkdir',
    full_name='rpcpb.SliverRPC.Mkdir',
    index=41,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._MKDIRREQ,
    output_type=sliverpb_dot_sliver__pb2._MKDIR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Download',
    full_name='rpcpb.SliverRPC.Download',
    index=42,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._DOWNLOADREQ,
    output_type=sliverpb_dot_sliver__pb2._DOWNLOAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='rpcpb.SliverRPC.Upload',
    index=43,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._UPLOADREQ,
    output_type=sliverpb_dot_sliver__pb2._UPLOAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ProcessDump',
    full_name='rpcpb.SliverRPC.ProcessDump',
    index=44,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._PROCESSDUMPREQ,
    output_type=sliverpb_dot_sliver__pb2._PROCESSDUMP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunAs',
    full_name='rpcpb.SliverRPC.RunAs',
    index=45,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._RUNASREQ,
    output_type=sliverpb_dot_sliver__pb2._RUNAS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Impersonate',
    full_name='rpcpb.SliverRPC.Impersonate',
    index=46,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._IMPERSONATEREQ,
    output_type=sliverpb_dot_sliver__pb2._IMPERSONATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RevToSelf',
    full_name='rpcpb.SliverRPC.RevToSelf',
    index=47,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._REVTOSELFREQ,
    output_type=sliverpb_dot_sliver__pb2._REVTOSELF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSystem',
    full_name='rpcpb.SliverRPC.GetSystem',
    index=48,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._GETSYSTEMREQ,
    output_type=sliverpb_dot_sliver__pb2._GETSYSTEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Task',
    full_name='rpcpb.SliverRPC.Task',
    index=49,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._TASKREQ,
    output_type=sliverpb_dot_sliver__pb2._TASK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Msf',
    full_name='rpcpb.SliverRPC.Msf',
    index=50,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._MSFREQ,
    output_type=commonpb_dot_common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MsfRemote',
    full_name='rpcpb.SliverRPC.MsfRemote',
    index=51,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._MSFREMOTEREQ,
    output_type=commonpb_dot_common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExecuteAssembly',
    full_name='rpcpb.SliverRPC.ExecuteAssembly',
    index=52,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._EXECUTEASSEMBLYREQ,
    output_type=sliverpb_dot_sliver__pb2._EXECUTEASSEMBLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Migrate',
    full_name='rpcpb.SliverRPC.Migrate',
    index=53,
    containing_service=None,
    input_type=clientpb_dot_client__pb2._MIGRATEREQ,
    output_type=sliverpb_dot_sliver__pb2._MIGRATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Execute',
    full_name='rpcpb.SliverRPC.Execute',
    index=54,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._EXECUTEREQ,
    output_type=sliverpb_dot_sliver__pb2._EXECUTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExecuteToken',
    full_name='rpcpb.SliverRPC.ExecuteToken',
    index=55,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._EXECUTETOKENREQ,
    output_type=sliverpb_dot_sliver__pb2._EXECUTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Sideload',
    full_name='rpcpb.SliverRPC.Sideload',
    index=56,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._SIDELOADREQ,
    output_type=sliverpb_dot_sliver__pb2._SIDELOAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SpawnDll',
    full_name='rpcpb.SliverRPC.SpawnDll',
    index=57,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._INVOKESPAWNDLLREQ,
    output_type=sliverpb_dot_sliver__pb2._SPAWNDLL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Screenshot',
    full_name='rpcpb.SliverRPC.Screenshot',
    index=58,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._SCREENSHOTREQ,
    output_type=sliverpb_dot_sliver__pb2._SCREENSHOT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NamedPipes',
    full_name='rpcpb.SliverRPC.NamedPipes',
    index=59,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._NAMEDPIPESREQ,
    output_type=sliverpb_dot_sliver__pb2._NAMEDPIPES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TCPListener',
    full_name='rpcpb.SliverRPC.TCPListener',
    index=60,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._TCPPIVOTREQ,
    output_type=sliverpb_dot_sliver__pb2._TCPPIVOT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListPivots',
    full_name='rpcpb.SliverRPC.ListPivots',
    index=61,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._PIVOTLISTREQ,
    output_type=sliverpb_dot_sliver__pb2._PIVOTLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartService',
    full_name='rpcpb.SliverRPC.StartService',
    index=62,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._STARTSERVICEREQ,
    output_type=sliverpb_dot_sliver__pb2._SERVICEINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopService',
    full_name='rpcpb.SliverRPC.StopService',
    index=63,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._STOPSERVICEREQ,
    output_type=sliverpb_dot_sliver__pb2._SERVICEINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveService',
    full_name='rpcpb.SliverRPC.RemoveService',
    index=64,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._REMOVESERVICEREQ,
    output_type=sliverpb_dot_sliver__pb2._SERVICEINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MakeToken',
    full_name='rpcpb.SliverRPC.MakeToken',
    index=65,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._MAKETOKENREQ,
    output_type=sliverpb_dot_sliver__pb2._MAKETOKEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEnv',
    full_name='rpcpb.SliverRPC.GetEnv',
    index=66,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._ENVREQ,
    output_type=sliverpb_dot_sliver__pb2._ENVINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetEnv',
    full_name='rpcpb.SliverRPC.SetEnv',
    index=67,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._SETENVREQ,
    output_type=sliverpb_dot_sliver__pb2._SETENV,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Backdoor',
    full_name='rpcpb.SliverRPC.Backdoor',
    index=68,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._BACKDOORREQ,
    output_type=sliverpb_dot_sliver__pb2._BACKDOOR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegistryRead',
    full_name='rpcpb.SliverRPC.RegistryRead',
    index=69,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._REGISTRYREADREQ,
    output_type=sliverpb_dot_sliver__pb2._REGISTRYREAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegistryWrite',
    full_name='rpcpb.SliverRPC.RegistryWrite',
    index=70,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._REGISTRYWRITEREQ,
    output_type=sliverpb_dot_sliver__pb2._REGISTRYWRITE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegistryCreateKey',
    full_name='rpcpb.SliverRPC.RegistryCreateKey',
    index=71,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._REGISTRYCREATEKEYREQ,
    output_type=sliverpb_dot_sliver__pb2._REGISTRYCREATEKEY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Shell',
    full_name='rpcpb.SliverRPC.Shell',
    index=72,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._SHELLREQ,
    output_type=sliverpb_dot_sliver__pb2._SHELL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTunnel',
    full_name='rpcpb.SliverRPC.CreateTunnel',
    index=73,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._TUNNEL,
    output_type=sliverpb_dot_sliver__pb2._TUNNEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseTunnel',
    full_name='rpcpb.SliverRPC.CloseTunnel',
    index=74,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._TUNNEL,
    output_type=commonpb_dot_common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TunnelData',
    full_name='rpcpb.SliverRPC.TunnelData',
    index=75,
    containing_service=None,
    input_type=sliverpb_dot_sliver__pb2._TUNNELDATA,
    output_type=sliverpb_dot_sliver__pb2._TUNNELDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Events',
    full_name='rpcpb.SliverRPC.Events',
    index=76,
    containing_service=None,
    input_type=commonpb_dot_common__pb2._EMPTY,
    output_type=clientpb_dot_client__pb2._EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SLIVERRPC)

DESCRIPTOR.services_by_name['SliverRPC'] = _SLIVERRPC

# @@protoc_insertion_point(module_scope)
