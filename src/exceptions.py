
class LocaldataException(Exception):
    pass


LocaldataErrors = {
    "002": {"code": "002", "message": "서비스 ID 값이 유효하지 않습니다.", "method": "서비스 ID 값을 확인바랍니다.(개편 전 API 신청자에 한정)"},
    "001": {"code": "001", "message": "서비스 ID 값이 정의되지 않았습니다.", "method": "서비스 ID 값을 확인바랍니다.(개편 전 API 신청자에 한정)"},
    "003": {"code": "003", "message": "검색 일자가 누락되었습니다.", "method": "검색 일자를 확인바랍니다."},
    "004": {"code": "004", "message": "검색 시작일자가 누락되었습니다.", "method": "검색 시작일자를 입력바랍니다.(시작일자와 종료일자는 동시 입력바랍니다.)"},
    "005": {"code": "005", "message": "검색 종료일자가 누락되었습니다.", "method": "검색 종료일자를 입력바랍니다.(시작일자와 종료일자는 동시 입력바랍니다.)"},
    "006": {"code": "006", "message": "검색일자 형식 오류입니다.", "method": "일자조회 시 YYYYMMDD 형식으로 입력바랍니다. (예:20150301)"},
    "007": {"code": "007", "message": "검색 일자 오류입니다.", "method": "검색 시작일자가 검색 종료일자보다 큽니다.	검색 일자 범위를 확인 바랍니다."},
    "008": {"code": "008", "message": "검색 조건으로 음의 값을 사용할 수 없는 숫자가 지정되었습니다.", "method": "양의 값의 숫자로 입력바랍니다."},
    "009": {"code": "009", "message": "숫자 형식 오류입니다.", "method": "숫자 형식에 맞게 입력바랍니다."},
    "010": {"code": "010", "message": "결과 형태가 유효하지 않습니다.", "method": "결과 형태를 확인바랍니다.(resultType : (def)xml, json / 파일로 받을 시- xlsx, xls, csv )"},
    "011": {"code": "011", "message": "영업 상태코드가 유효하지 않습니다.", "method": "state변수에 들어갈 수 있는 값은 01,02,03,04 입니다.(01: 영업/정상, 02:휴업, 03: 폐업, 04: 취소/말소/만료/정지/중지)"},
    "015": {"code": "015", "message": "전 월의 24일 이후만 가능합니다.", "method": "lastModTsBgn값을 확인 바랍니다."},
    "016": {"code": "016", "message": "현재일 이전만 가능합니다.", "method": "endYmd 또는 lastModTsEnd 값을 확인 바랍니다."},
    "098": {"code": "098", "message": "오픈API 요청 데이터건수가 개발용-500건/운영용-10,000건을 초과하였습니다.", "method": "state, pageSize, pageIndex 요청값을 추가하여 조회하시기 바랍니다.(pageSize 개발용 최대 - 500/ 운영용 최대 - 10,000)"},
    "099": {"code": "099", "message": "오픈API 호출간격이 짧습니다.", "method": "잠시 후 다시 시도해 주시기 바랍니다."},
    "801": {"code": "801", "message": "파일다운로드 오류", "method": "잠시 후 다시 시도 바랍니다."},
    "902": {"code": "902", "message": "해당 OPENAPI의 서비스 권한이 존재하지 않습니다.", "method": "API유형코드 및 인증키를 확인바랍니다."},
    "999": {"code": "999", "message": "알 수 없는 시스템 오류가 발생하였습니다.", "method": "관리자에게 문의 바랍니다."}
}