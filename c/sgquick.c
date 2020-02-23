#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


#include "sginfo.h"


static int str_ibegin(const char *s1, const char *s2) /* string ignore-case */  // 判断两个字符串是否相同
{                                                     /* begin              */
  char     u1, u2;

  while (*s1 && *s2) // 遍历字符串
  {
    u1 = toupper(*s1++);  // toupper将小写字母都转化为大写
    u2 = toupper(*s2++);
    if      (u1 < u2) return -1;  // 当出现不相同的字符时直接返回
    else if (u1 > u2) return  1;
  }
  if (*s2) return -1; // 当"VolA"没有遍历完说明结果也没有对应，同样返回错误结果
  return 0; // 如果前面没有问题则正常返回
}


int BuildSgInfo(T_SgInfo *SgInfo, const char *SgName) // 形参为SgInfo结构体地址和SgName地址, const用于不可修改变量
{
  int                VolLetter;
  const T_TabSgName  *tsgn;  // T_TabDgName结构体


  /* look for "VolA", "VolI", or "Hall"
   */

  while (*SgName && isspace(*SgName)) SgName++;  // 判断字符否存在，isspace()判断字符是否为空格或制表符等，是返回1。这里用于排除命令行字符串中的空格，直到出现字符为止

  VolLetter = -1;

  if      (isdigit(*SgName))  // 检查相应字符串是否为数字字符，如果是则判断为VolA
    VolLetter = 'A';
  else if (str_ibegin(SgName, "VolA") == 0)  // 判断字符串是否为"VolA"
  {
    VolLetter = 'A';
    SgName += 4;  // 地址前进一位
  }
  else if (   str_ibegin(SgName, "VolI") == 0
           || str_ibegin(SgName, "Vol1") == 0) // 判断字符串是否为"VolI"或"Vol1"
  {
    VolLetter = 'I';
    SgName += 4;
  }
  else if (str_ibegin(SgName, "Hall") == 0) // 判断字符串是否为'Hall'
  {
    VolLetter = 0;
    SgName += 4;
  }

  while (*SgName && isspace(*SgName)) SgName++;  // 除去空格，直到识别空间群字符串

  /* default is "VolA"
   */

  if (VolLetter == -1)  // 默认值
    VolLetter = 'A';

  /* if we don't have a Hall symbol do a table look-up
   */

  tsgn = NULL;  // 将地址tsgn设为空值

/*如果存在VolLetter, 通诺FindTabSgNameEntry()查找空间群，参数为定位到空间群字符串地址SgName和代表空间群符号类型的VolLetter*/
  if (VolLetter)
  {
    tsgn = FindTabSgNameEntry(SgName, VolLetter);
    if (tsgn == NULL) return -1; /* no matching table entry */ //没有查找到则直接返回
    SgName = tsgn->HallSymbol; // 通过tsgn结构体获取HallSymbol
  }

  /* Allocate memory for the list of Seitz matrices and
     a supporting list which holds the characteristics of
     the rotation parts of the Seitz matrices
   */

  SgInfo->MaxList = 192; /* absolute maximum number of symops */  // 设置SgInfo结构体MaxList元素值

  SgInfo->ListSeitzMx
    = malloc(SgInfo->MaxList * sizeof (*SgInfo->ListSeitzMx)); // 为LsitSeitzMx申请内存

  if (SgInfo->ListSeitzMx == NULL) {
    SetSgError("Not enough core");
    return -1;
  }  // 对应地址为Null,说明没有申请到内存

  SgInfo->ListRotMxInfo
    = malloc(SgInfo->MaxList * sizeof (*SgInfo->ListRotMxInfo)); // 同样为ListRotMxInfo申请内存

  if (SgInfo->ListRotMxInfo == NULL) {
    SetSgError("Not enough core");
    return -1;
  }

  /* Initialize the SgInfo structure
   */

  InitSgInfo(SgInfo);  // 初始化SgInfo结构体
  SgInfo->TabSgName = tsgn; /* in case we know the table entry */  // 将地址tegn赋值给SgInfo元素TabSgName

  /* Translate the Hall symbol and generate the whole group
   */

  ParseHallSymbol(SgName, SgInfo);  // 获取所有对称性操作矩阵
  if (SgError != NULL) return -1;

  /* Do some book-keeping and derive crystal system, point group,
     and - if not already set - find the entry in the internal
     table of space group symbols
   */

  return CompleteSgInfo(SgInfo);  
}


int main(int argc, char *argv[])  // 命令行输入参数
{
  T_SgInfo  SgInfo;   // 创建SgInfo结构体


  if (argc == 2)  // 当命令行有两个参数时
  {
    if (BuildSgInfo(&SgInfo, argv[1]) != 0)  // 解析命令行参数，查找相应空间群，如果不能正常返回则按标准错误流输出结果
      fprintf(stderr, "%s\n", SgError);
    else
    {
      ListSgInfo(&SgInfo, 1, 0, stdout); // 如果执行没有问题则打印输出结果

      if (SgError)
        fprintf(stderr, "%s\n", SgError);
    }
  }

  return 0;  // 正常输出
}
